# Getting Started

```shell
fastflow init
```

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
