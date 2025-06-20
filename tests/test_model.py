from pathlib import Path
from typing import ClassVar

from deflow.assets.models import AbstractModel


class TestAbstractModel(AbstractModel):
    check_type: ClassVar[str] = "Pipeline"


def test_abs_model(test_path: Path):
    data = TestAbstractModel.from_conf(
        "p_pipe_cm_d", path=test_path / "v2/conf"
    )
    assert data.type == "Pipeline"
    print(data)

    print(data.get_variable(env="prod"))
