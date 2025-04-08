from ddeutil.workflow import config

from deflow.flow import Flow


def test_flow_stream():
    print(config.conf_path)
    stream_flow = Flow("s_cm_d")
    print(stream_flow)


def test_flow_stream_run():
    stream_flow = Flow("s_cm_d")
    rs = stream_flow.run(mode="N")
    print(rs.context)
