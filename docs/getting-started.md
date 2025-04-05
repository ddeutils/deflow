# Getting Started

## Initialize

Start initialize local data framework with the `init` CLI.

```shell
deflow init
```

The output project structure that was auto created from the initialize command:

```text
conf
    - c
    - s
    - s_stream_name
```

## Running Flow

```python
from deflow.flow import Flow

flow = Flow(name="s_stream_name_d").run(mode="N")
```
