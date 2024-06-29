from dataclasses import dataclass,asdict,astuple

@dataclass(frozen=True)
class application:
    identifier:str
    interfaces:str
    platform:str
    target:str
    args:tuple
    workers:tuple
    broker:str
    data:str
    policies:tuple = tuple()