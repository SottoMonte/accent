from dataclasses import dataclass,asdict,astuple

@dataclass(frozen=True)
class application:
    type:str
    channel:str
    pattern:str
    data:tuple