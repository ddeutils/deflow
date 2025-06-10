from pathlib import Path

from ddeutil.workflow import Result

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
            "registry_caller": ["tests.v2"],
            "deflow_conf_path": test_path / "conf/v2",
        },
    )
    rs: Result = flow.run(mode="N")
    print(rs.context)
