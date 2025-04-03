from fastflow.io import get_process


def test_io_get_process(test_path):
    data = get_process(name="p_first", path=test_path / "conf")
    print(data)
