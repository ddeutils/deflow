from pathlib import Path

from deflow.utils import get_data

from .utils import exclude_created_and_updated


def test_get_data(test_path: Path):
    data = get_data("p_pipe_cm_d", path=test_path / "v2/conf")
    assert exclude_created_and_updated(data["conf"]) == {
        "name": "p_pipe_cm_d",
        "type": "Pipeline",
        "owner": "data-team",
        "schedule": "@daily",
        "start_date": "2025-01-01",
        "tags": ["example", "cm"],
        "dir_path": test_path / "v2/conf/pipeline/p_pipe_cm_d",
    }
    print(data["children"])
    print(data)
