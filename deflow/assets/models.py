import copy
from datetime import datetime
from pathlib import Path
from textwrap import dedent
from typing import Callable, ClassVar, Literal, Optional, Union

from ddeutil.workflow import get_dt_now
from pydantic import BaseModel, Field
from pydantic.functional_validators import field_validator
from typing_extensions import Self

from ..__types import DictData
from ..utils import get_data

RunMode = Literal["N", "R", "F", "T"]
GetConfigFunc = Callable[[str, Path], DictData]


class AbstractModel(BaseModel):
    """Abstract model for any data framework model."""

    get_data: ClassVar[GetConfigFunc] = get_data
    check_type: ClassVar[Optional[str]] = None

    conf_dir: Path = Field(description="A dir path of this config data.")
    name: str = Field(description="A config name.")
    type: str = Field(
        description="A type of config. It should be the same as model name."
    )
    desc: str = Field(
        default=None,
        description=(
            "A description of this config that allow writing with the markdown "
            "syntax."
        ),
    )
    created_at: datetime = Field(
        default_factory=get_dt_now,
        description=(
            "A created datetime of this config data when loading from " "file."
        ),
    )
    updated_at: datetime = Field(
        default_factory=get_dt_now,
        description=(
            "A updated datetime of this config data when loading from " "file."
        ),
    )
    tags: list[str] = Field(
        default_factory=list,
        description="A list of tag for simple group this config.",
    )

    @field_validator("desc", mode="after")
    def __dedent_desc__(cls, data: str) -> str:
        """Prepare description string that was created on a template.

        Args:
            data: A description string value that want to dedent.

        Returns:
            str: The de-dented description string.
        """
        return dedent(data.lstrip("\n"))

    @classmethod
    def from_conf(cls, name: str, path: Path) -> Self:
        """Construct Pipeline model from an input pipeline name and config path.

        :param name: (str) A pipeline name that want to search from config path.
        :param path: (Path) A config path.

        :rtype: Self
        """
        data: DictData = cls.get_data(name=name, path=path)
        if (t := data["conf"].get("type")) != (cls.check_type or cls.__name__):
            raise ValueError(
                f"Type {t!r} does not match with "
                f"{(cls.check_type or cls.__name__)!r}."
            )

        loader_data: DictData = copy.deepcopy(data["conf"])
        return cls.model_validate(obj=loader_data)

    def get_variable(self, env: str) -> DictData:
        import yaml

        variable = Variable.model_validate(
            obj=yaml.safe_load((self.conf_dir / "variables.yml").open())
        )
        return variable.get_env(env)


class Variable(BaseModel):
    stages: dict[str, dict[str, Union[str, int]]] = Field(default_factory=dict)

    def get_env(self, env: str) -> DictData:
        if env not in self.stages:
            raise ValueError
        return self.stages[env]
