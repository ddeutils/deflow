from pathlib import Path

import pytest

from .utils import dotenv_setting

dotenv_setting()


@pytest.fixture(scope="session")
def test_path():
    return Path(__file__).parent
