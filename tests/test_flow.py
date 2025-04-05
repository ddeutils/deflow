from ddeutil.workflow import config, make_registry

from deflow.flow import Flow


def test_flow_stream():
    print(config.conf_path)

    stream_flow = Flow("s_first_d")
    print(stream_flow)


def test_flow_stream_run():
    print(config.regis_call)

    registries = make_registry("tasks")
    print(registries)

    stream_flow = Flow("s_first_d")
    stream_flow.run(mode="N")
