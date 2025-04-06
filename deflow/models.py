# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import BaseModel, Field
from typing_extensions import Self

from .conf import config
from .utils import get_process


class Frequency(BaseModel):
    type: str
    offset: int = 1


class Stream(BaseModel):
    name: str = Field(description="A stream name")


class Group(BaseModel):
    name: str = Field(description="A group name")
    tier: Literal["bronze", "silver", "gold"]
    priority: int


class Dependency(BaseModel):
    name: str
    offset: int = Field(default=1)


class Connection(BaseModel):
    ir: Optional[str] = Field(default=None)
    service: str
    host: str
    database: str
    user: str
    secret: str = Field(
        description="A secret key for getting from any secret manager service.",
    )


class System(BaseModel):
    name: str
    container: str
    path: str


class TestDataset(BaseModel):
    file: Optional[str] = Field(default=None)


class Dataset(BaseModel):
    conn: str = Field(alias="conn")
    scm: str = Field(alias="schema")
    tbl: str = Field(alias="table")
    sys: Optional[str] = Field(default=None, alias="system")
    tests: TestDataset = Field(default_factory=TestDataset)


class Process(BaseModel):
    """Process model."""

    name: str = Field(description="A process name.")
    stream: Stream = Field(description="A stream of this group.")
    group: Group = Field(description="A group of this process.")
    routing: int = Field(description="A routing value for running workflow.")
    load_type: str
    priority: int
    source: Dataset
    target: Dataset
    extras: dict[str, Any] = Field(default_factory=dict)
    deps: list[Dependency] = Field(
        default_factory=list,
        description="List of process dependency.",
    )

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
            process.stream.name == stream_name
        ), "Stream does not match with file location."
        return process
