# DeFlow

A **Lightweight Declarative Data Workflow Framework** (DeFlow) that build on the
[🏃Workflow](https://github.com/ddeutils/ddeutil-workflow) package.

> [!WARNING]
> This framework does not allow you to custom your pipeline yet. If you want to
> create you workflow, you can use the [🏃Workflow](https://github.com/ddeutils/ddeutil-workflow)
> package instead that already installed.

## 📦 Installation

```shell
pip install -U deflow
```

## 🍻 Usage

The data pipeline config will store with this file structure:

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

## 💬 Contribute

I do not think this project will go around the world because it has specific propose,
and you can create by your coding without this project dependency for long term
solution. So, on this time, you can open [the GitHub issue on this project 🙌](https://github.com/ddeutils/fastflow/issues)
for fix bug or request new feature if you want it.
