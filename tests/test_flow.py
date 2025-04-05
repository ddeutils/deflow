from deflow.flow import Flow


def test_flow_stream():
    stream_flow = Flow("s_first_d")
    print(stream_flow)


def test_flow_stream_run():
    stream_flow = Flow("s_first_d")
    stream_flow.run(mode="N")
