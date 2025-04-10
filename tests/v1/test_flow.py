from ddeutil.workflow import Result

from deflow.flow import Flow


def test_flow():
    flow = Flow("s_cm_d")
    print(flow)


def test_flow_run():
    flow = Flow("s_cm_d")
    rs: Result = flow.run(mode="N")
    print(rs.context)
