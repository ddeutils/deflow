from pathlib import Path

from deflow.assets.v1.core.utils import get_stream


def test_v1_utils_get_stream(test_path: Path):
    data = get_stream(name="s_cm_d", path=test_path / "v1/conf")
    assert data == {
        "type": "Stream",
        "date_frequency": {"type": "daily"},
        "frequency": {"offset": 1, "type": "daily"},
        "groups": {
            "g_first": {
                "processes": {
                    "p_first_process_01": {
                        "name": "p_first_process_01",
                        "group_name": "g_first",
                        "stream_name": "s_cm_d",
                        "deps": [
                            {"name": "p_deps_process_01", "offset": 1},
                            {"name": "p_deps_process_02", "offset": 1},
                        ],
                        "load_type": "F",
                        "priority": 1,
                        "source": {
                            "conn": "name",
                            "extras": {
                                "container": "container-name",
                                "header": True,
                                "sheet_name": "product",
                                "path": "path-name",
                            },
                            "schema": "source/%Y%m%d",
                            "table": "product.xlsx",
                            "tests": {"file": "name/source/product.xlsx"},
                        },
                        "target": {
                            "conn": "product",
                            "schema": "dwh",
                            "table": "bronze",
                            "extras": {
                                "container": "container-name",
                                "path": "path-name",
                            },
                        },
                        "routing": 1,
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
                        "group_name": "g_second",
                        "stream_name": "s_cm_d",
                        "deps": [
                            {"name": "p_deps_process_01", "offset": 1},
                            {"name": "p_deps_process_02", "offset": 1},
                        ],
                        "extras": {"archive": True},
                        "load_type": "F",
                        "priority": 1,
                        "routing": 2,
                        "source": {
                            "conn": "name",
                            "schema": "publish",
                            "table": "province",
                            "extras": {"system": "ms"},
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
            "g_third": {
                "processes": {
                    "p_third_process_01": {
                        "name": "p_third_process_01",
                        "group_name": "g_third",
                        "stream_name": "s_cm_d",
                        "deps": [
                            {
                                "name": "p_deps_process_01",
                                "offset": 1,
                            },
                            {
                                "name": "p_deps_process_02",
                                "offset": 1,
                            },
                        ],
                        "extras": {
                            "archive": True,
                        },
                        "load_type": "F",
                        "priority": 1,
                        "routing": 2,
                        "source": {
                            "conn": "name",
                            "extras": {
                                "system": "ms",
                            },
                            "schema": "publish",
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
                "name": "g_third",
                "tier": "bronze",
                "priority": "2",
            },
        },
    }
