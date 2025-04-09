import pytest


@pytest.fixture(scope="session")
def version_path(test_path):
    return test_path.parent / "deflow/assets/v1"
