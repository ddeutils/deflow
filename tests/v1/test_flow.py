from datetime import datetime

from ddeutil.workflow import SUCCESS, Result

from deflow.flow import Flow


def test_flow():
    flow = Flow(name="s_cm_d", version="v1")
    assert flow.name == "s_cm_d"
    assert flow.version == "v1"


def test_flow_run():
    flow = Flow(
        name="s_cm_d",
        version="v1",
        extras={"deflow_registry_caller": ["tests.v1"]},
    )
    rs: Result = flow.run(mode="N")
    assert rs.status == SUCCESS
    print(rs.context)


def test_flow_run_with_dt():
    flow = Flow(
        name="s_cm_d",
        version="v1",
        extras={
            "enable_write_audit": False,
            "deflow_registry_caller": ["tests.v1"],
        },
    )
    rs: Result = flow.run(dt=datetime(2025, 5, 16), mode="N")
    assert rs.status == SUCCESS
    print(rs.context)
