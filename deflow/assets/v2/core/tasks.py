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

from ddeutil.workflow import Result, tag

from ....__types import DictData
from ....conf import config
from .models import Node, Pipeline

VERSION: str = "v2"
TAG_VERSION_2 = partial(tag, name=VERSION)


@TAG_VERSION_2(alias="get-start-pipeline-info")
def get_start_pipeline_info(name: str, result: Result) -> DictData:
    """Get Stream model information. This function use to validate an input
    stream name that exists on the config path.

    :param name: (str) A stream name
    :param result: (Result) A result dataclass for make logging.

    :rtype: DictData
    """
    result.trace.info(f"Start getting stream: {name!r} info.")
    pipeline: Pipeline = Pipeline.from_conf(name=name, path=config.conf_path)
    result.trace.info(
        f"... Start Stream Info:"
        f"||=> freq: {pipeline.freq.model_dump(by_alias=True)}"
        f"||=> data_freq: {pipeline.data_freq.model_dump(by_alias=True)}"
    )

    return {
        "name": pipeline.name,
        "freq": pipeline.freq.model_dump(by_alias=True),
        "data_freq": pipeline.data_freq.model_dump(by_alias=True),
        "priority-groups": sorted(pipeline.priority_group().keys()),
        "stream": pipeline.model_dump(by_alias=True),
        "audit-date": datetime(2025, 4, 1, 1),
        "logical-date": datetime(2025, 4, 1, 1),
    }


@TAG_VERSION_2(alias="start-node")
def start_node(name: str, result: Result) -> DictData:
    """Start process with an input process name.

    :param name: (str) A process name.
    :param result: (Result) A result dataclass for make logging.
    """
    result.trace.info(f"Start getting process: {name!r} info")
    process: Node = Node.from_conf(name=name, path=config.conf_path)
    result.trace.info(f"... routing of this process: {process.routing}")
    return {
        "routing": process.routing,
        "process": process.model_dump(by_alias=True),
    }
