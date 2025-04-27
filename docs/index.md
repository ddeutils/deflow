# DeFlow

A **Lightweight Declarative Data Framework** that build on the
[🏃 Workflow](https://github.com/ddeutils/ddeutil-workflow) package.

I want to use this project is the real-world use-case for my [🏃 Workflow](https://github.com/ddeutils/ddeutil-workflow)
package that able to handle production data pipeline with the DataOps strategy.

!!! warning

    This framework does not allow you to custom your pipeline yet. If you want to
    create you workflow, you can use the [🏃 Workflow](https://github.com/ddeutils/ddeutil-workflow)
    package instead that already installed.

In my opinion, I think it should not create duplicate workflow codes if I can
write with dynamic input parameters on the one template workflow that just change
the input parameters per use-case instead.
This way I can handle a lot of logical workflows in our orgs with only metadata
configuration. It called **Metadata Driven Data Workflow**.

## 📦 Installation

```shell
pip install -U deflow
```

## 💬 Contribute

I do not think this project will go around the world because it has specific propose,
and you can create by your coding without this project dependency for long term
solution. So, on this time, you can open [the GitHub issue on this project 🙌](https://github.com/ddeutils/fastflow/issues)
for fix bug or request new feature if you want it.
