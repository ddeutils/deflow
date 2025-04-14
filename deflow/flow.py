# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from datetime import datetime
from typing import Optional

from ddeutil.workflow import Result, Workflow
from ddeutil.workflow import config as workflow_config

from .__types import DictData
from .conf import ASSETS_PATH, config


def routing_workflow(
    name: str, version: str, *, extras: Optional[DictData] = None
) -> Workflow:
    extras: DictData = {
        **{
            "conf_path": ASSETS_PATH / f"{config.version}/templates",
            "audit_path": workflow_config.audit_path / f"stream={name}",
            "registry_caller": [f"deflow.assets.{config.version}.core"],
        },
        **(extras or {}),
    }
    if version == "v1":
        return Workflow.from_conf("stream-workflow", extras=extras)
    raise NotImplementedError(f"Flow version: {version!r} does not implement.")


class Flow:
    """Flow object for manage workflow model release and test via configuration.
    This is the core object for this package that active data pipeline from
    the current data framework version.

    :param name: (str) A stream name.
    :param extras: (DictData) An extra parameters that want to override the
        workflow config.
    :param version: (str) A version of data framework that want creates Workflow
        model.
    """

    def __init__(
        self,
        name: str,
        *,
        extras: Optional[DictData] = None,
        version: Optional[str] = None,
    ) -> None:
        self.name: str = name
        self.version: str = version or config.version
        self.extras: DictData = extras or {}
        self.workflow: Workflow = routing_workflow(
            name, version=self.version, extras=self.extras
        )

    def __repr__(self) -> str:
        """Override __repr__ method."""
        return f"{self.__class__.__name__}(name={self.name})"

    def __str__(self) -> str:
        """Override __str__ method."""
        return self.name

    def run(self, mode: str) -> Result:
        """Start release dynamic pipeline with this flow name.

        :param mode: (str) A running mode of this flow.
        """
        return self.workflow.release(
            release=datetime.now(),
            params={
                "name": self.name,
                "run-mode": mode,
            },
        )

    def test(self) -> Result:
        """Test running flow on local without integration testing."""
        return self.run(mode="TEST")

    def ui(self): ...
