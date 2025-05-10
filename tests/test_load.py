import pytest
from ddeutil.workflow.conf import FileLoad


def test_file_load(test_path):
    loader = FileLoad(name="s_cm_d", path=test_path / "conf/v1")
    assert loader.data == {
        "type": "Stream",
        "frequency": {"type": "daily", "offset": 1},
        "date_frequency": {"type": "daily"},
    }

    # NOTE: Raise if config data does not found because it was ignored.
    with pytest.raises(ValueError):
        FileLoad(name="s_ignore_d", path=test_path / "conf/v1")
