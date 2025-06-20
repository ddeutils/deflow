import pytest

from deflow.flow import Flow


def test_flow_unsupported_version():
    with pytest.raises(NotImplementedError):
        Flow(name="hello-world", version="v99")
