from typing import Literal

from pydantic import BaseModel, Field


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
    def load_conf(cls, name: str): ...
