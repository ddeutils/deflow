from ddeutil.workflow import tag


@tag("v1", alias="get-stream-info")
def get_stream_info(name: str):
    return {"name": name}
