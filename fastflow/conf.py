import os
from pathlib import Path


class Config:

    @property
    def root_path(self) -> Path:
        return Path(os.getenv("FASTFLOW_ROOT_PATH"))

    @property
    def conf_path(self) -> Path:
        return self.root_path / os.getenv("FASTFLOW_CONF_PATH", "conf")


config = Config()
