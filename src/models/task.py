from typing import TypedDict
from datetime import datetime

class Task(TypedDict):
    id: int
    description: str
    status: str
    createdAt: datetime
    updatedAt: datetime
    