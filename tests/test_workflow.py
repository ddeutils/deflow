from ddeutil.workflow import Result, Workflow, extract_call

from deflow.conf import config


def test_workflow():
    workflow = Workflow.from_conf("stream-workflow")
    rs: Result = workflow.execute(
        params={
            "stream": "s_cm_d",
            "run_mode": "N",
        }
    )
    print(rs.context)


def test_extract_call():
    func = extract_call(
        "tasks/get-stream-info@v1",
        registries=[f"deflow.assets.{config.version}"],
    )
    print(func)
