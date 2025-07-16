from pathlib import Path

import pytest

from deflow.assets.utils import get_conf, search_conf_parent_path

from .utils import exclude_created_and_updated


def test_search_conf_parent_path(test_path: Path):
    assert (
        search_conf_parent_path("01", path=test_path / "conf")
        == test_path / "conf/abstract/usage/01"
    )

    with pytest.raises(FileNotFoundError):
        search_conf_parent_path(
            "01", path=test_path / "conf", name_key="app_name"
        )


def test_get_conf(test_path: Path):
    data = get_conf("01", path=test_path / "conf")
    assert exclude_created_and_updated(data["conf"]) == {
        "name": "01",
        "tags": ["demo", "abstract"],
        "type": "AbstractModel",
        "conf_dir": test_path / "conf/abstract/usage/01",
    }
    assert [c["path"] for c in data["children"]] == [
        Path("child_01.yml"),
        Path("child_02.yml"),
        Path("child_03.yml"),
        Path("assets/01.sql"),
    ]
    print(data["children"])
