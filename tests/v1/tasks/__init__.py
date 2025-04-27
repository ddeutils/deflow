# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from datetime import datetime

from ddeutil.workflow import Result, tag

from deflow.__types import DictData
from deflow.assets.v1.core.models import Process


@tag("v1", alias="routing-01")
def routing_ingest_file(
    process: Process,
    audit_date: datetime,
    result: Result,
) -> DictData:
    """Routing file.

    :param process: (Process)
    :param audit_date: (datetime)
    :param result: (Result)
    """
    result.trace.info(f"[CALLER]: Routing: 01 with process: {process.name!r}")
    result.trace.info(
        "[CALLER]: ... This routing is ingest data with file type."
    )
    result.trace.info(f"[CALLER]: ... Audit date: {audit_date}")
    return {
        "records": 1000,
    }


@tag("v1", alias="routing-02")
def routing_ingest_db(
    process: Process,
    audit_date: datetime,
    result: Result,
) -> DictData:
    """Routing database.

    :param process: (Process)
    :param audit_date: (datetime)
    :param result: (Result)
    """
    result.trace.info(f"[CALLER]: Routing: 02 with process: {process.name!r}")
    result.trace.info(
        "[CALLER]: ... This routing is ingest data with database type."
    )
    result.trace.info(f"[CALLER]: ... Audit date: {audit_date}")
    return {
        "records": 1000,
    }
