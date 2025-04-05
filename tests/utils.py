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
            WORKFLOW_CONF_ROOT_PATH={OUTSIDE_PATH.absolute()}
            WORKFLOW_CORE_REGISTRY=fastflow
            WORKFLOW_CORE_CONF_PATH=fastflow/templates
            WORKFLOW_CORE_TIMEZONE=Asia/Bangkok
            WORKFLOW_CORE_STAGE_DEFAULT_ID=true
            WORKFLOW_CORE_STAGE_RAISE_ERROR=true
            WORKFLOW_CORE_JOB_DEFAULT_ID=false
            WORKFLOW_CORE_JOB_RAISE_ERROR=true
            WORKFLOW_CORE_GENERATE_ID_SIMPLE_MODE=true
            WORKFLOW_CORE_MAX_NUM_POKING=4
            WORKFLOW_CORE_MAX_JOB_PARALLEL=1
            WORKFLOW_CORE_MAX_JOB_EXEC_TIMEOUT=600
            WORKFLOW_CORE_MAX_CRON_PER_WORKFLOW=5
            WORKFLOW_CORE_MAX_QUEUE_COMPLETE_HIST=16
            WORKFLOW_LOG_PATH={(OUTSIDE_PATH / "logs").absolute()}
            WORKFLOW_LOG_ENABLE_WRITE=true
            WORKFLOW_AUDIT_PATH={(OUTSIDE_PATH / "audits").absolute()}
            WORKFLOW_AUDIT_ENABLE_WRITE=true
            FASTFLOW_CORE_ROOT_PATH={OUTSIDE_PATH.absolute()}
            FASTFLOW_CORE_CONF_PATH=tests/conf
            """
        ).strip()
        env_path.write_text(env_str)

    load_dotenv(env_path)
