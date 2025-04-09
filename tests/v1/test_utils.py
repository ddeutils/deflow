from pathlib import Path

from deflow.assets.v1.core.utils import get_stream


def test_v1_utils_get_stream(test_path: Path):
    data = get_stream(name="s_cm_d", path=test_path / "conf")
    assert data == {
        "type": "Stream",
        "date_frequency": {"type": "daily"},
        "frequency": {"offset": 1, "type": "daily"},
        "groups": {
            "g_first": {
                "processes": {
                    "p_first_process_01": {
                        "name": "p_first_process_01",
                        "deps": [
                            {"name": "p_deps_process_01", "offset": 1},
                            {"name": "p_deps_process_02", "offset": 1},
                        ],
                        "etl": {
                            "load_type": "F",
                            "priority": 1,
                            "source": {
                                "connection": "name",
                                "extras": {
                                    "header": True,
                                    "sheet_name": "product",
                                },
                                "schema": "source/%Y%m%d",
                                "system": {
                                    "container": "container-name",
                                    "path": "path-name",
                                },
                                "table": "product.xlsx",
                                "tests": {"file": "name/source/product.xlsx"},
                            },
                            "target": {
                                "connection": "product",
                                "schema": "dwh",
                                "system": {
                                    "container": "container-name",
                                    "path": "path-name",
                                },
                                "table": "bronze",
                            },
                            "type": 1,
                        },
                        "type": "Process",
                    }
                },
                "name": "g_first",
                "tier": "bronze",
                "priority": "1",
            },
            "g_second": {
                "processes": {
                    "p_second_process_01": {
                        "name": "p_second_process_01",
                        "deps": [
                            {"name": "p_deps_process_01", "offset": 1},
                            {"name": "p_deps_process_02", "offset": 1},
                        ],
                        "extras": {"archive": True},
                        "load_type": "F",
                        "priority": 1,
                        "routing": 1,
                        "source": {
                            "conn": "name",
                            "schema": "publish",
                            "system": "ms",
                            "table": "province",
                        },
                        "target": {
                            "conn": "dwh",
                            "schema": "bronze",
                            "table": "province",
                        },
                        "type": "Process",
                    }
                },
                "name": "g_second",
                "tier": "bronze",
                "priority": "1",
            },
        },
    }


def test_v1_utils_get_process(test_path):
    # data = get_process(name="p_first", path=test_path / "conf")
    # print(data)
    ...
