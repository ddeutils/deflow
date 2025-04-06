from ddeutil.workflow import Result, Workflow


def test_workflow():
    workflow = Workflow.from_conf("stream-workflow")
    rs: Result = workflow.execute(
        params={
            "stream": "s_first_d",
            "run_mode": "N",
        }
    )
    print(rs.context)
