from pathlib import Path

from ddeutil.workflow import SUCCESS, Result

from deflow.flow import Flow


def test_flow():
    flow = Flow(name="p_pipe_cm_d", version="v2")
    assert flow.name == "p_pipe_cm_d"
    assert flow.version == "v2"


def test_flow_run(test_path: Path):
    flow = Flow(
        name="p_pipe_cm_d",
        version="v2",
        extras={
            "deflow_registry_caller": ["tests.v2"],
            "deflow_conf_path": test_path / "v2/conf",
        },
    )
    rs: Result = flow.run(mode="N")
    assert rs.status == SUCCESS
    print(rs.context)
