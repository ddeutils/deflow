# Configuration

| Name                            | Component | Default  | Description                                        |
|:--------------------------------|:---------:|:---------|:---------------------------------------------------|
| **DEFLOW_CORE_CONF_PATH**       |   CORE    | `./conf` | A config path to get data framework configuration. |
| **DEFLOW_CORE_VERSION**         |   CORE    | `v1`     | A specific data framework version.                 |
| **DEFLOW_CORE_REGISTRY_CALLER** |   CORE    | `.`      | A registry of caller function.                     |

**Support data framework version:**

| Version | Supported | Description                                                     |
|:-------:|:---------:|:----------------------------------------------------------------|
|    1    | Progress  | A data framework that base on `stream`, `group`, and `process`. |
|    2    | Progress  | A data framework that base on `pipeline`, and `node`.           |
