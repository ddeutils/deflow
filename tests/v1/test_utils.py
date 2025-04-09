from pathlib import Path

from deflow.assets.v1.core.utils import get_group, get_stream


def test_v1_utils_get_process(test_path):
    # data = get_process(name="p_first", path=test_path / "conf")
    # print(data)
    ...


def test_v1_utils_get_stream(test_path: Path):
    data = get_stream(name="s_cm_d", path=test_path / "conf")
    assert data == {
        "type": "Stream",
        "frequency": {"offset": 1, "type": "daily"},
        "date_frequency": {"type": "daily"},
    }


def test_v1_utils_get_group(test_path: Path):
    data = get_group(stream="s_cm_d", path=test_path / "conf")
    print(data)
