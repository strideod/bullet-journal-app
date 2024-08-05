import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Task(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")