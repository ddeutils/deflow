from pathlib import Path

from deflow.utils import get_data


def test_get_data(test_path: Path):
    get_data("p_pipe_cm_d", path=test_path / "conf/v2")
