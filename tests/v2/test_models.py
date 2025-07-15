from pathlib import Path

import pytest

from deflow.assets.v2.core import Node, Pipeline


def test_pipeline(test_path):
    pipeline: Pipeline = Pipeline.from_conf(
        name="p_pipe_cm_d", path=test_path / "v2/conf"
    )
    assert pipeline.name == "p_pipe_cm_d"
    print()
    print(pipeline)
    # assert pipeline.node_priorities() == [["n_node_01"], ["n_node_02"]]


def test_pipeline_load_ignore(test_path: Path):
    assert (test_path / "v2/conf/pipeline/p_pipe_ignore_d").exists()
    assert (
        "p_pipe_ignore_d/\n" in (test_path / "v2/conf/.confignore").read_text()
    )

    with pytest.raises(FileNotFoundError):
        Pipeline.from_conf(name="p_pipe_ignore_d", path=test_path / "v2/conf")


def test_node(test_path: Path):
    node: Node = Node.from_conf(name="n_node_01", path=test_path / "v2/conf")
    assert node.name == "n_node_01"
    print(node.assets)
    assert node.assets == ["assets/n_node_01.json"]
    assets = node.asset(node.assets[0])
    print(assets)
