import uuid
from datetime import datetime
from enum import Enum
from typing import Optional, Union
from pydantic import BaseModel, Field

class LogType(str, Enum):
    task = "task"
    note = "note"
    event = "event"

class TaskStatus(str, Enum):
    incomplete = "incomplete"
    task_completed = " task completed"
    task_migrated = "task migrated"
    task_scheduled = "task scheduled"
    task_irrelevant = "task irrelevant"

class BaseLog(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    type: LogType = Field(...)
    date: datetime = Field(default_factory=lambda: datetime.now())
    description: str = Field(...)
    

    class Config:
        allow_population_by_field_name = True

class Task(BaseLog):
    status: TaskStatus = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "_id": "00000000-0000-0000-0000-000000000000",
                "type": "task",
                "description": "get bread",
                "status" : "task completed"
            }
        }

class Note(BaseLog):

    class Config:
        schema_extra = {
            "example": {
                "_id": "00000000-0000-0000-0000-000000000000",
                "type": "note",
                "description": "Smith is details 1st person",
            }
        }

class Event(BaseLog):
    event_date: Optional[str] = None
    event_time: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "_id": "00000000-0000-0000-0000-000000000000",
                "type": "event",
                "description": "birthday party",
                "event_date": "2024-08-15",
                "event_time": "1300"
            }
        }

class UpdateBaseLog(BaseModel):
    type: Optional[LogType]
    description: Optional[str]


DailyLog = Union[Task, Note, Event]