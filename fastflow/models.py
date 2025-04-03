from typing import Literal

from pydantic import BaseModel, Field
from typing_extensions import Self

from .conf import config
from .utils import get_process


class Stream(BaseModel):
    name: str = Field(description="A stream name")
    active: bool = Field(default=True)


class Group(BaseModel):
    name: str = Field(description="A group name")
    stream: Stream = Field(description="A stream of this group")
    type: Literal["bronze", "silver", "gold"]
    active: bool = Field(default=True)


class Process(BaseModel):
    name: str = Field(description="A process name")
    group: Group = Field(description="A group of this process")
    active: bool = Field(default=True)

    @classmethod
    def load_conf(cls, name: str) -> Self:
        data = get_process(name, path=config.conf_path)
        group_name = data.pop("group_name")
        stream_name = data.pop("stream_name")
        process = cls.model_validate(obj=data)
        assert (
            process.group.name == group_name
        ), "Group does not match with file location."
        assert (
            process.group.stream.name == stream_name
        ), "Stream does not match with file location."
        return process
