from ddeutil.workflow import Result, Workflow, extract_call

from deflow.conf import config


def test_workflow(test_path):
    workflow = Workflow.from_conf(
        "stream-workflow",
        extras={
            "conf_path": (
                test_path.parent / f"deflow/assets/{config.version}/templates"
            )
        },
    )
    rs: Result = workflow.execute(
        params={
            "stream": "s_cm_d",
            "run-mode": "N",
        }
    )
    print(rs.context)


def test_extract_call():
    func = extract_call(
        "tasks/get-stream-info@v1",
        registries=[f"deflow.assets.{config.version}"],
    )
    print(func)
