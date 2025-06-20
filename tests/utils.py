# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

import logging
from pathlib import Path
from textwrap import dedent

from dotenv import load_dotenv

OUTSIDE_PATH: Path = Path(__file__).parent.parent


def dotenv_setting() -> None:
    """Create .env file if this file in the current path does not exist."""
    env_path: Path = OUTSIDE_PATH / ".env"
    if not env_path.exists():
        logging.warning("Dot env file does not exists")
        # NOTE: For ``CONF_ROOT_PATH`` value on the different OS:
        #   * Windows: D:\user\path\...\ddeutil-workflow
        #   * Ubuntu: /home/runner/work/ddeutil-workflow/ddeutil-workflow
        #
        env_str: str = dedent(
            f"""
            WORKFLOW_LOG_TIMEZONE=Asia/Bangkok
            WORKFLOW_LOG_TRACE_URL=file:{(OUTSIDE_PATH / "logs/traces").absolute()}
            WORKFLOW_LOG_TRACE_ENABLE_WRITE=true
            WORKFLOW_LOG_AUDIT_URL=file:{(OUTSIDE_PATH / "logs/audits").absolute()}
            WORKFLOW_LOG_AUDIT_ENABLE_WRITE=true
            DEFLOW_CORE_CONF_PATH={(OUTSIDE_PATH / "tests/conf/v1").absolute()}
            DEFLOW_CORE_REGISTRY_CALLER=tests.v1
            """
        ).strip()
        env_path.write_text(env_str)

    load_dotenv(env_path)
