from ddeutil.workflow.conf import SimLoad


def test_simload(test_path):
    loader = SimLoad(name="s_first_d", conf_path=test_path / "conf")
    print(loader.data)
