from deflow.models import Group, Process, Stream


def test_models_stream():
    stream = Stream.model_validate(
        obj={
            "name": "s_first_d",
            "frequency": {"type": "daily", "offset": 1},
            "date_frequency": {"type": "daily"},
        }
    )
    print(stream)


def test_models_group():
    group = Group.model_validate(
        obj={
            "name": "g_first",
            "tier": "bronze",
            "priority": 1,
        }
    )
    print(group)


def test_models_process():
    stream = Stream.model_validate(
        obj={
            "name": "s_first_d",
            "frequency": {"type": "daily", "offset": 1},
            "date_frequency": {"type": "daily"},
        }
    )

    group = Group.model_validate(
        obj={
            "name": "g_first",
            "tier": "bronze",
            "priority": 1,
        }
    )

    process = Process.model_validate(
        obj={
            "name": "p_first_process_01",
            "stream": stream,
            "group": group,
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
