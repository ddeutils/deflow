import pytest
from ddeutil.workflow.conf import SimLoad


def test_simload(test_path):
    loader = SimLoad(name="s_cm_d", conf_path=test_path / "conf")
    print(loader.data)


def test_simload_ignore(test_path):

    with pytest.raises(ValueError):
        SimLoad(name="s_ignore_d", conf_path=test_path / "conf")
