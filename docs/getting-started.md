# Getting Started

## Initialize

Start initialize local data framework with the `init` CLI.

```shell
deflow init
```

The output project structure that was auto created from the initialize command:

```text
conf/
 ├─ conn/
 │   ├─ c_conn_01.yml
 │   ╰─ c_conn_02.yml
 ╰─ stream/
     ╰─ s_stream_01/
         ├─ g_group_01.tier.priority/
         │   ├─ p_proces_01.yml
         │   ╰─ p_proces_02.yml
         ├─ g_group_02.tier.priority/
         │   ├─ p_proces_01.yml
         │   ╰─ p_proces_02.yml
         ╰─ s_stream_01.yml
```

## Running Flow

```python
from deflow.flow import Flow

flow = Flow(name="s_stream_name_d").run(mode="N")
```
