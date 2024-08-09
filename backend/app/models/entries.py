import uuid
from datetime import datetime
from enum import Enum
from typing import Optional, Union
from pydantic import BaseModel, Field

class EntryType(str, Enum):
    task = "task"
    note = "note"
    event = "event"

class TaskStatus(str, Enum):
    incomplete = "incomplete"
    task_completed = " task completed"
    task_migrated = "task migrated"
    task_scheduled = "task scheduled"
    task_irrelevant = "task irrelevant"

class BaseEntry(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    type: EntryType = Field(...)
    date: datetime = Field(default_factory=lambda: datetime.now())
    description: str = Field(...)
    

    class Config:
        populate_by_name = True

class Task(BaseEntry):
    status: TaskStatus = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "00000000-0000-0000-0000-000000000000",
                "type": "task",
                "description": "get bread",
                "status" : "task completed"
            }
        }

class Note(BaseEntry):

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "00000000-0000-0000-0000-000000000000",
                "type": "note",
                "description": "Smith is details 1st person",
            }
        }

class Event(BaseEntry):
    event_date: Optional[str] = None
    event_time: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "_id": "00000000-0000-0000-0000-000000000000",
                "type": "event",
                "description": "birthday party",
                "event_date": "2024-08-15",
                "event_time": "1300"
            }
        }

class UpdateBaseEntry(BaseModel):
    type: Optional[EntryType]
    description: Optional[str]


Entry = Union[Task, Note, Event]