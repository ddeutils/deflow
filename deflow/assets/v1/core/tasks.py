# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from datetime import datetime
from functools import partial

from ddeutil.workflow import Result, tag

from ....__types import DictData
from ....conf import config
from .models import Frequency, Stream

VERSION: str = "v1"
tag_v1 = partial(tag, name=VERSION)


@tag_v1(alias="get-stream-info")
def get_stream_info(name: str, result: Result) -> DictData:
    """Get Stream model information.

    :param name: (str) A stream name
    :param result: (Result) A result dataclass for make logging.

    :rtype: DictData
    """
    result.trace.info(f"[CALLER]: Start getting stream: {name!r} information.")
    stream: Stream = Stream.from_path(name=name, path=config.conf_path)
    return {
        "name": stream.name,
        "freq": stream.freq.model_dump(),
        "data_freq": stream.data_freq.model_dump(),
        "priority-groups": stream.priority_group(),
    }


@tag_v1(alias="start-stream")
def start_stream(
    name: str, freq: Frequency, data_freq: Frequency, result: Result
) -> DictData:
    """Start stream workflow with update audit watermarking and generate starter
    stream log.

    :param name: (str) A stream name that want to get audit logs for generate
        the next audit date.
    :param freq: (Frequency) A audit date frequency.
    :param data_freq: (Frequency) A logical date frequency.
    :param result: (Result) A result dataclass for make logging.
    """
    result.trace.info(f"[CALLER]: Start running stream: {name!r}.")
    result.trace.info(f"... freq: {freq}")
    result.trace.info(f"... data_freq: {data_freq}")
    return {
        "audit-date": datetime(2025, 4, 1, 1),
        "logical-date": datetime(2025, 4, 1, 1),
    }


@tag_v1(alias="get-groups-from-priority")
def get_groups_from_priority(priority: int, result: Result):
    result.trace.info(f"[CALLER]: Get groups from priority: {priority}")
    if priority == 1:
        result.trace.info("... Return groups from 1")
        return {"groups": ["group-01", "group-02"]}
    else:
        result.trace.info("... Return groups from 2")
        return {"groups": ["group-03"]}


@tag_v1(alias="get-processes-from-group")
def get_processes_from_group(group: str, result: Result):
    result.trace.info(f"[CALLER]: Get processes from group: {group}")
    if group == "group-01":
        return {"processes": ["process-01"]}
    elif group == "group-02":
        return {"processes": ["process-02"]}
    else:
        return {"processes": ["process-03"]}
