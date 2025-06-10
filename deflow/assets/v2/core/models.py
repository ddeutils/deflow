import copy
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field
from typing_extensions import Self

from ....__types import DictData
from .utils import get_pipeline


class NodeDeps(BaseModel):
    name: str
    trigger_rule: Optional[str] = Field(default=None)


class Node(BaseModel):
    name: str
    desc: Optional[str] = Field(default=None)
    upstream: list[NodeDeps] = Field(default_factory=list)


class Lineage(BaseModel):
    inlets: list[NodeDeps] = Field(default_factory=list)
    outlets: list[NodeDeps] = Field(default_factory=list)


class Pipeline(BaseModel):
    """Pipeline model."""

    name: str = Field(description="A pipeline.")
    desc: Optional[str] = Field(
        default=None,
        description=(
            "A pipeline description that allow to write with markdown syntax."
        ),
    )
    nodes: dict[str, Node] = Field(
        default_factory=list, description="A list of Node model."
    )
    tags: list[str] = Field(default_factory=list)

    @classmethod
    def from_conf(cls, name: str, path: Path) -> Self:
        """Construct Pipeline model from an input pipeline name and config path.

        :param name: (str) A pipeline name that want to search from config path.
        :param path: (Path) A config path.

        :rtype: Self
        """
        data: DictData = get_pipeline(name=name, path=path)

        if (t := data.pop("type")) != cls.__name__:
            raise ValueError(f"Type {t!r} does not match with {cls}")

        loader_data: DictData = copy.deepcopy(data)
        loader_data["name"] = name

        return cls.model_validate(obj=loader_data)

    def node(self, name: str) -> Node:
        return self.nodes[name]
