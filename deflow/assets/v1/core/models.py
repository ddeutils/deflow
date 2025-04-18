# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

import copy
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Literal, Optional
from zoneinfo import ZoneInfo

from pydantic import BaseModel, Field
from typing_extensions import Self

from deflow.__types import DictData

from .utils import get_process, get_stream


class Frequency(BaseModel):
    """Frequency model for generate audit date."""

    type: Literal["daily", "monthly", "yearly", "hourly"] = Field(
        default="daily",
        description="A frequency type.",
    )
    offset: int = Field(
        default=1,
        description="An offset value for decrease freq type unit.",
    )

    def gen_datetime(
        self, dt: Optional[datetime] = None, tz: Optional[ZoneInfo] = None
    ) -> datetime:
        """Generate and prepare datetime"""
        tz = tz or ZoneInfo("UTC")
        if dt is None:
            dt = datetime.now(tz=tz)
        return dt - timedelta(days=self.offset)


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
    groups: dict[str, Group] = Field(
        default_factory=dict,
        description="A list of Group model.",
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

    def group(self, name: str) -> Group:
        """Get a Group model by name.

        :param name: (str) A group name.

        :rtype: Group
        """
        return self.groups[name]

    def priority_group(self) -> dict[int, list[Group]]:
        """Return the ordered list of distinct group priority that keep in this
        stream.

        :rtype: dict[int, list[Group]]
        """
        rs: dict[int, list[Group]] = {}
        for group in self.groups.values():
            if group.priority in rs:
                rs[group.priority].append(group)
            else:
                rs[group.priority] = [group]
        return rs


GroupTier = Literal["raw", "bronze", "silver", "gold", "staging", "operation"]


class Group(BaseModel):
    """Group model that use for grouping process together and run with its
    priority.
    """

    name: str = Field(description="A group name")
    tier: GroupTier = Field(description="A tier of this group.")
    priority: int = Field(gt=0, description="A priority of this group.")
    processes: dict[str, Process] = Field(
        default_factory=dict,
        description="A list of Process model.",
    )

    @property
    def filename(self) -> str:
        """Return the file name that combine name, tier, and priority of this
        group.

        :rtype: str
        """
        return f"{self.name}.{self.tier}.{self.priority}"

    def process(self, name: str) -> Process:
        return self.processes[name]


class Dependency(BaseModel):
    name: str = Field(description="A dependency process name.")
    offset: int = Field(default=1)


class Connection(BaseModel):
    ir: Optional[str] = Field(default=None)
    service: str
    host: str
    database: str
    user: str
    secret: Optional[str] = Field(
        default=None,
        description="A secret key for getting from any secret manager service.",
    )


class System(BaseModel):
    name: str
    container: str
    path: str


class TestDataset(BaseModel):
    file: Optional[str] = Field(default=None)


class Dataset(BaseModel):
    """Dataset model."""

    conn: str = Field(alias="conn", description="A connection name.")
    scm: str = Field(
        alias="schema", description="A schema or parent path name."
    )
    tbl: str = Field(alias="table", description="A table or file name.")
    tests: TestDataset = Field(default_factory=TestDataset)


class Process(BaseModel):
    """Process model for only one action for move the data from source to
    target with routing type.
    """

    name: str = Field(description="A process name.")
    stream: Optional[str] = None
    group: Optional[str] = None
    routing: int = Field(
        ge=1, lt=20, description="A routing value for running workflow."
    )
    load_type: str = Field(description="A loading type.")
    priority: int = Field(gt=0, description="A priority of this process.")
    source: Dataset
    target: Dataset
    extras: dict[str, Any] = Field(default_factory=dict)
    deps: list[Dependency] = Field(
        default_factory=list,
        description="List of process dependency.",
    )

    @classmethod
    def from_path(cls, name: str, path: Path) -> Self:
        data = get_process(name=name, path=path)

        if (t := data.pop("type")) != cls.__name__:
            raise ValueError(f"Type {t!r} does not match with {cls}")

        loader_data: DictData = copy.deepcopy(data)
        return cls.model_validate(obj=loader_data)


class Dates(BaseModel):
    audit_date: datetime
    logical_date: datetime
