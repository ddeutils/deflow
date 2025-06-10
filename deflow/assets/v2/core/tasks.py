# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
"""The Core Tasks module for keeping necessary tasks that use on the caller
stage that config in the workflow template.
"""
from __future__ import annotations

from datetime import datetime
from functools import partial
from typing import Any

from ddeutil.workflow import Result, tag

from ....__types import DictData
from ....conf import dynamic
from .models import Node, Pipeline

VERSION: str = "v2"
TAG_VERSION_2 = partial(tag, name=VERSION)


@TAG_VERSION_2(alias="get-start-pipeline-info")
def get_start_pipeline_info(
    name: str, result: Result, extras: dict[str, Any]
) -> DictData:
    """Get Pipeline model information. This function use to validate an input
    pipeline name that exists on the config path.

    :param name: (str) A pipeline name
    :param result: (Result) A result dataclass for make logging.
    :param extras: (dict[str, Any]) An extra parameters.

    :rtype: DictData
    """
    result.trace.info(f"Start getting pipeline: {name!r} info.")
    pipeline: Pipeline = Pipeline.from_conf(
        name=name, path=dynamic("deflow_conf_path", extras=extras)
    )
    result.trace.info(f"... Start Pipeline Info:||" f"> {pipeline}")

    return {
        "name": pipeline.name,
        "stream": pipeline.model_dump(by_alias=True),
        "audit-date": datetime(2025, 4, 1, 1),
        "logical-date": datetime(2025, 4, 1, 1),
    }


@TAG_VERSION_2(alias="start-node")
def start_node(name: str, result: Result, extras: dict[str, Any]) -> DictData:
    """Start process with an input process name.

    :param name: (str) A process name.
    :param result: (Result) A result dataclass for make logging.
    :param extras: (dict[str, Any]) An extra parameters.
    """
    result.trace.info(f"Start getting process: {name!r} info")
    process: Node = Node.from_conf(
        name=name, path=dynamic("deflow_conf_path", extras=extras)
    )
    return {
        "process": process.model_dump(by_alias=True),
    }
