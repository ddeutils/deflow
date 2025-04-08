# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

import copy
from datetime import datetime
from pathlib import Path
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field
from typing_extensions import Self

from .__types import DictData
from .conf import config
from .utils import get_process, get_stream


class Frequency(BaseModel):
    """Frequency model for generate audit date."""

    type: str = Field(
        default="daily",
        description="A frequency type.",
    )
    offset: int = Field(
        default=1, description="An offset value for decrease freq type unit."
    )


class Stream(BaseModel):
    """Stream model."""

    name: str = Field(description="A stream name")
    freq: Frequency = Field(
        default_factory=Frequency,
        description="A frequency",
        alias="frequency",
    )
    data_freq: Frequency = Field(
        default_factory=Frequency,
        description="A data frequency",
        alias="date_frequency",
    )

    @classmethod
    def from_path(cls, name: str, path: Path) -> Self:
        """Construct Stream model from an input stream name and config path.

        :param name: (str) A stream name that want to search from config path.
        :param path: (Path) A config path.

        :rtype: Self
        """
        data = get_stream(name=name, path=path)

        if (t := data.pop("type")) != cls.__name__:
            raise ValueError(f"Type {t!r} does not match with {cls}")

        loader_data: DictData = copy.deepcopy(data)
        loader_data["name"] = name
        return cls.model_validate(obj=loader_data)


class Group(BaseModel):
    name: str = Field(description="A group name")
    tier: Literal["bronze", "silver", "gold"]
    priority: int

    @classmethod
    def from_stream(cls, name: str, path: Path) -> Self:
        """Construct Group model from an input stream name and config path."""
        return


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


class Dates(BaseModel):
    audit_date: datetime
    logical_date: datetime
