from pathlib import Path

from deflow.utils import get_stream


def test_utils_get_process(test_path):
    # data = get_process(name="p_first", path=test_path / "conf")
    # print(data)
    ...


def test_utils_get_stream(test_path: Path):
    data = get_stream(name="s_cm_d", path=test_path / "conf")
    print(data)
