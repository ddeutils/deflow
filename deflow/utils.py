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
    """Get Stream data."""
    for file in path.rglob("*"):
        if file.is_dir() and file.stem == name:
            print(file)


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
                    f"Get process file: {file.name} does not support for "
                    f"type: {file.suffix}."
                )
    raise FileNotFoundError(f"{path}/**/{name}.yml")
