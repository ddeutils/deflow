from pathlib import Path

from deflow.assets.v2.core import Node, Pipeline


def test_pipeline(test_path):
    pipeline: Pipeline = Pipeline.from_conf(
        name="p_pipe_cm_d", path=test_path / "conf/v2"
    )
    assert pipeline.name == "p_pipe_cm_d"
    assert pipeline.lineage() == [["n_node_01"], ["n_node_02"]]


def test_node(test_path: Path):
    node: Node = Node.from_conf(name="n_node_01", path=test_path / "conf/v2")
    assert node.name == "n_node_01"
    print(node.assets)
    assets = node.asset(node.assets[0])
    print(assets)
