# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Optional

from ddeutil.workflow import Result, Workflow

from .__types import DictData
from .conf import config

ASSETS_PATH: Path = Path(__file__).parent / "assets"


class Flow:
    """Flow object for manage workflow model release and test via configuration.

    :param name: (str) A stream name.
    :param extras: (DictData) An extra parameters that want to override the
        workflow config.
    """

    def __init__(
        self,
        name: str,
        extras: Optional[DictData] = None,
    ) -> None:
        self.name: str = name
        self.extras: DictData = {
            **{
                "conf_path": ASSETS_PATH / f"{config.version}/templates",
                "regis_call": [f"deflow.assets.{config.version}"],
            },
            **(extras or {}),
        }
        self.workflow: Workflow = Workflow.from_conf(
            "stream-workflow",
            extras=self.extras,
        )

    def run(self, mode: str) -> Result:
        """Start release dynamic pipeline with this flow name."""
        return self.workflow.release(
            release=datetime.now(),
            params={
                "name": self.name,
                "run-mode": mode,
            },
        )

    def test(self) -> Result:
        """Test."""
        return self.run(mode="TEST")
