from fastflow.models import Process


def test_models_process():
    process = Process.model_validate(
        {
            "name": "process-name",
            "group": {
                "name": "group-name",
                "stream": {
                    "name": "stream-name",
                },
                "type": "bronze",
            },
        }
    )
    print(process)
