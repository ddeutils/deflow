from pydantic import BaseModel, Field


class NodeDeps(BaseModel):
    name: str
    trigger_rule: str


class Node(BaseModel):
    name: str
    desc: str
    upstream: list[NodeDeps] = Field(default_factory=list)


class Pipeline(BaseModel):
    name: str
    desc: str
    nodes: list[Node] = Field(default_factory=list)
