from deflow.assets.v1.core.models import Group, ProcessDirect, Stream


def test_v1_models_stream():
    stream = Stream.model_validate(
        obj={
            "name": "s_first_d",
            "frequency": {"type": "daily", "offset": 1},
            "date_frequency": {"type": "daily"},
        }
    )
    print(stream)
    assert stream.groups == {}
    assert stream.priority_group() == []


def test_v1_models_stream_from_path(test_path):
    stream = Stream.from_path("s_cm_d", path=test_path / "conf")
    print(stream)
    print(stream.priority_group())
    assert stream.priority_group() == [1, 2]


def test_v1_models_group():
    group = Group.model_validate(
        obj={
            "name": "g_first",
            "tier": "bronze",
            "priority": 1,
        }
    )
    print(group)


def test_v1_models_process():
    process = ProcessDirect.model_validate(
        obj={
            "name": "p_first_process_01",
            "stream": "s_cm_d",
            "group": "g_first",
            "routing": 1,
            "load_type": "F",
            "priority": 1,
            "source": {
                "conn": "name",
                "schema": "source/%Y%m%d",
                "table": "product.xlsx",
                "system": "hm",
                "extras": {"header": True},
            },
            "target": {
                "conn": "name",
                "schema": "foo",
                "table": "bar",
            },
            "extras": {"archive": True},
            "deps": [
                {"name": "p_deps_process_01", "offset": 1},
                {"name": "p_deps_process_02", "offset": 1},
            ],
        }
    )
    print(process)
