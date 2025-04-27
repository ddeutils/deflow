from ddeutil.workflow import Result

from deflow.flow import Flow


def test_flow():
    flow = Flow("s_cm_d", version="v1")
    assert flow.name == "s_cm_d"
    assert flow.version == "v1"


def test_flow_run():
    flow = Flow(
        "s_cm_d",
        version="v1",
        extras={"registry_caller": ["tests.v1"]},
    )
    rs: Result = flow.run(mode="N")
    print(rs.context)
