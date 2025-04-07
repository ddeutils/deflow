# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from pathlib import Path

from ddeutil.io import YamlEnvFl

from .__types import DictData


def get_stream(name: str, path: Path) -> DictData:
    """Get Stream data that store on an input config path.

    :param name:
    :param path:

    :rtype: DictData
    """
    for file in path.rglob("*"):
        if file.is_dir() and file.stem == name:
            cfile: Path = file / "config.yml"
            if not cfile.exists():
                raise FileNotFoundError(
                    f"Get stream file: {cfile.name} does not exist."
                )

            data: DictData = YamlEnvFl(path=cfile).read()
            if name not in data:
                raise ValueError(
                    f"Stream config does not set {name!r} config data."
                )
            elif "type" not in (stream_data := data[name]):
                raise ValueError(
                    "Stream config does not pass the `type` for validation."
                )
            return stream_data

    raise FileNotFoundError(f"Does not found stream: {name!r} at {path}")


def get_process(name: str, path: Path) -> DictData:
    """Get Process data from an input name and path values.

    :param name: (str)
    :param path: (Path)

    :rtype: dict[str, Any]
    """
    for file in path.rglob("*"):
        if file.is_file() and file.stem == name:
            if file.suffix in (".yml", ".yaml"):
                data = YamlEnvFl(path=file).read()
                return {
                    "name": name,
                    "group_name": file.parent.name,
                    "stream_name": file.parent.parent.name,
                    **data,
                }
            else:
                raise NotImplementedError(
                    f"Get process file: {file.name} does not support for file"
                    f"type: {file.suffix}."
                )
    raise FileNotFoundError(f"{path}/**/{name}.yml")
