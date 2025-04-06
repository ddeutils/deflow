# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from .__types import DictData


class FlowType(str, Enum):
    STREAM: str = "stream"
    GROUP: str = "group"
    PROCESS: str = "process"


def get_workflow(flow_type: FlowType, extras: Optional[DictData] = None):
    from ddeutil.workflow import Workflow

    if flow_type == FlowType.STREAM:
        return Workflow.from_conf("stream-workflow", extras=extras)
    elif flow_type == FlowType.GROUP:
        return Workflow.from_conf("group-workflow", extras=extras)
    else:
        return Workflow.from_conf("process-workflow", extras=extras)


class Flow:
    def __init__(
        self,
        name: str,
        flow_type: FlowType = FlowType.STREAM,
        extras: Optional[DictData] = None,
    ):
        self.name = name
        self.type = flow_type
        self.workflow = get_workflow(flow_type, extras=extras)

    def run(self, mode: str):
        self.workflow.release(
            release=datetime.now(),
            params={
                "stream": self.name,
                "run-mode": mode,
            },
        )
