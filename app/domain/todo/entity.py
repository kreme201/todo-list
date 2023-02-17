from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    id: int = 0
    status: bool = False
    content: str = ""
    created: datetime = datetime.now()
