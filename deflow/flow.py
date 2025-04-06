# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from datetime import datetime
from typing import Optional

from ddeutil.workflow import Result, Workflow

from .__types import DictData


class Flow:
    def __init__(
        self,
        name: str,
        extras: Optional[DictData] = None,
    ):
        self.name = name
        self.workflow: Workflow = Workflow.from_conf(
            "stream-workflow", extras=extras
        )

    def run(self, mode: str) -> Result:
        """Start release dynamic pipeline with this flow name."""
        return self.workflow.release(
            release=datetime.now(),
            params={
                "stream": self.name,
                "run-mode": mode,
            },
        )

    def test(self): ...
