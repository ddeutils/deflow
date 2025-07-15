import copy
from pathlib import Path
from typing import ClassVar, cast
from unittest.mock import patch

from deflow.__types import DictData
from deflow.assets.models import AbstractModel
from deflow.utils import ConfData, get_data


def mock_load_conf(
    cls: AbstractModel, name: str, path: Path
) -> DictData:  # pragma: no cov
    return {
        "name": name,
        "conf_dir": path / "abstract/usage/01",
        "type": cls.__name__,
    }


@patch.multiple(AbstractModel, __abstractmethods__=set())
def test_abstract_model(test_path: Path):
    assert AbstractModel.load_conf("01", path=test_path / "conf") is None

    AbstractModel.load_conf = classmethod(mock_load_conf)
    data = AbstractModel.from_conf("01", path=test_path / "conf")
    assert data.name == "01"
    print(data)
    print(data.get_variable(env="prod"))


class MockAbstractModel(AbstractModel):  # pragma: no cov
    check_type: ClassVar[str] = "AbstractModel"

    @classmethod
    def load_conf(cls, name: str, path: Path) -> DictData:
        data: ConfData = get_data(name=name, path=path)
        if (t := data["conf"].get("type")) != (cls.check_type or cls.__name__):
            raise ValueError(
                f"Type {t!r} does not match with "
                f"{(cls.check_type or cls.__name__)!r}."
            )
        return cast(DictData, copy.deepcopy(data))["conf"]


def test_abstract_model_inherit(test_path):
    model = MockAbstractModel.from_conf("01", path=test_path / "conf")
    print(model)
