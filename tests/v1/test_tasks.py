from ddeutil.workflow import Result

from deflow.assets.v1.core.tasks import get_start_stream_info


def test_get_stream_info():
    rs: Result = Result(extras={"enable_write_log": False})
    data = get_start_stream_info(name="s_cm_d", result=rs, extras={})
    print(data)
