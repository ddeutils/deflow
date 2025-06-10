# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from pathlib import Path
from typing import Any

from ddeutil.io import YamlEnvFl

from ....__types import DictData


def get_pipeline(name: str, path: Path) -> DictData:
    """Get Pipeline data that store on an input config path.

    :param name: A pipeline name that want to search and extract data from the
        config path.
    :param path: A config path.

    :rtype: DictData
    """
    file: Path
    for file in path.rglob("*"):
        if file.is_dir() and file.stem == name:
            cfile: Path = file / "config.yml"
            if not cfile.exists():
                raise FileNotFoundError(
                    f"Get pipeline file: {cfile.name} does not exist."
                )

            data: DictData = YamlEnvFl(path=cfile).read()
            if name not in data:
                raise ValueError(
                    f"Pipeline config does not set {name!r} config data."
                )
            elif "type" not in (pipeline_data := data[name]):
                raise ValueError(
                    "Pipeline config does not pass the `type` for validation."
                )

            nodes: dict[str, Any] = {}
            f: Path
            for f in file.rglob("*"):
                if not f.is_file():
                    continue

                if file.suffix not in (".yml", ".yaml"):
                    continue

                node_data = YamlEnvFl(path=f).read()
                if node_data:
                    for name in node_data:
                        nodes[name] = {"name": name, **data[name]}

            pipeline_data["nodes"] = nodes
            return pipeline_data

    raise FileNotFoundError(f"Does not found pipeline: {name!r} at {path}")


def get_node(name: str, path: Path): ...
