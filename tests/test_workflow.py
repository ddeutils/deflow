from ddeutil.workflow import Result, Workflow, extract_call

from deflow.conf import config


def test_workflow(test_path):
    workflow = Workflow.from_conf(
        "stream-workflow",
        extras={
            "conf_path": (
                test_path.parent / f"deflow/assets/{config.version}/templates"
            ),
            "registry_caller": [f"deflow.assets.{config.version}.core"],
        },
    )
    rs: Result = workflow.execute(
        params={
            "name": "s_cm_d",
            "run-mode": "N",
        }
    )
    print(rs.context)


def test_extract_call():
    func = extract_call(
        "tasks/get-start-stream-info@v1",
        registries=[f"deflow.assets.{config.version}.core"],
    )
    print(func)
