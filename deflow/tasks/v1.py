from functools import partial

from ddeutil.workflow import Result, tag

VERSION: str = "v1"
tag_v1 = partial(tag, name=VERSION)


@tag_v1(alias="get-stream-info")
def get_stream_info(name: str):
    return {"name": name}


@tag_v1(alias="get-priority-group")
def get_priority_group(stream: str, result: Result):
    result.trace.info(f"Start get priority group: {stream}")
    return {"items": [1, 2]}
