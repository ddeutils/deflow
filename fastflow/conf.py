import os
from pathlib import Path


class Config:

    @property
    def conf_path(self) -> Path:
        return Path(os.getenv("FASTFLOW_CONF_PATH"))


config = Config()
