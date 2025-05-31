from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class BaseDataClass:
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
