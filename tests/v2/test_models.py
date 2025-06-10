from deflow.assets.v2.core import Pipeline


def test_pipeline(test_path):
    pipeline: Pipeline = Pipeline.from_conf(
        name="p_pipe_cm_d", path=test_path / "conf/v2"
    )
    assert pipeline.name == "p_pipe_cm_d"
    assert pipeline.lineage() == [["n_node_01"], ["n_node_02"]]
