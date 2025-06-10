# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

from datetime import datetime

from ddeutil.workflow import Result, tag

from deflow.__types import DictData
from deflow.assets.v2.core import Node


@tag(name="local", alias="import-file")
def operator_import_file(
    node: Node,
    audit_date: datetime,
    result: Result,
) -> DictData:
    """Operator for EL the file data source.

    :param node: (str) A node model.
    :param audit_date: (datetime)
    :param result: (Result)
    """
    result.trace.info(f"Call: import-file@local with node: {node.name!r}")
    result.trace.info("... This routing is ingest data with file type.")
    result.trace.info(
        f"... Audit date: {audit_date}||> params: {node.params}||"
    )
    return {
        "records": 1000,
    }


@tag(name="sqlite", alias="import-db")
def operator_import_db(
    node: Node,
    audit_date: datetime,
    result: Result,
) -> DictData:
    """Operator for EL the database data source.

    :param node: (str) A node model.
    :param audit_date: (datetime)
    :param result: (Result)
    """
    result.trace.info(f"Call: import-db@sqlite with node: {node.name!r}")
    result.trace.info("... This routing is ingest data with database type.")
    result.trace.info(
        f"... Audit date: {audit_date}||> params: {node.params}||"
    )
    return {
        "records": 1000,
    }
