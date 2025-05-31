from dataclasses import dataclass
from base.schema import BaseDataClass


@dataclass
class JwtTokenPair(BaseDataClass):
    refresh: str
    access: str
