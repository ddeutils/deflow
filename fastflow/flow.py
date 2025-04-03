from datetime import datetime


class StreamFlow:
    def __init__(self, name: str):
        self.name = name

    def run(self, mode: str):
        from ddeutil.workflow import Workflow

        workflow = Workflow.from_loader("stream-workflow")
        workflow.release(
            release=datetime.now(),
            params={
                "stream": self.name,
                "run-mode": mode,
            },
        )
