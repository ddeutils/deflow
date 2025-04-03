from fastflow.flow import StreamFlow


def test_flow_stream():
    stream_flow = StreamFlow("s_first_d")
    print(stream_flow)


def test_flow_stream_run():
    stream_flow = StreamFlow("s_first_d")
    stream_flow.run(mode="N")
