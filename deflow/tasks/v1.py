from datetime import datetime
from functools import partial

from ddeutil.workflow import Result, tag

VERSION: str = "v1"
tag_v1 = partial(tag, name=VERSION)


@tag_v1(alias="get-stream-info")
def get_stream_info(name: str):
    return {"name": name}


@tag_v1(alias="start-stream")
def start_stream(name: str):
    return {
        "audit-date": datetime(2025, 4, 1, 1),
    }


@tag_v1(alias="get-priority-group")
def get_priority_group(stream: str, result: Result):
    result.trace.info(f"Start get priority group: {stream}")
    return {"items": [1, 2]}


@tag_v1(alias="get-groups-from-priority")
def get_groups_from_priority(priority: int, result: Result):
    result.trace.info(f"Get groups from priority: {priority}")
    if priority == 1:
        return {"groups": ["group-01", "group-02"]}
    else:
        return {"groups": ["group-03"]}


@tag_v1(alias="get-processes-from-group")
def get_processes_from_group(group: str, result: Result):
    result.trace.info(f"Get processes from group: {group}")
    if group == "group-01":
        return {"processes": ["process-01"]}
    elif group == "group-02":
        return {"processes": ["process-02"]}
    else:
        return {"processes": ["process-03"]}
