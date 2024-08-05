from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.models import DailyLog, UpdateBaseLog

router=APIRouter()

@router.post("/", response_description="Create a new task", status_code=status.HTTP_201_CREATED, response_model=DailyLog)
def create_task(request: Request, task: DailyLog = Body(...)):
    task = jsonable_encoder(task)
    new_task = request.app.database["tasks"].insert_one(task)
    created_task = request.app.database["tasks"].find_one(
        {"_id": new_task.inserted_id}
    )

    return created_task

@router.get("/", response_description="List all tasks", response_model=List[DailyLog])
def list_daily_tasks(request: Request):
    tasks = list(request.app.database["tasks"].find(limit=100))
    return tasks

@router.get("/{id}", response_description="Get a single task by id", response_model=DailyLog)
def find_task(id: str, request: Request):
    if (task := request.app.database["tasks"].find_one({"_id": id})) is not None:
        return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found.")

@router.put("/{id}", response_description="Update a task", response_model=DailyLog)
def update_task(id: str, request: Request, task: UpdateBaseLog = Body(...)):
    task = {k: v for k, v in task.model_dump().items() if v is not None}
    if len(task) >= 1:
        update_result = request.app.database["tasks"].update_one(
            {"_id": id}, {"$set": task}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with ID {id} not found.")
    
    if (
        existing_book := request.app.database["tasks"].find_one({"_id": id})
    ) is not None:
        return existing_book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found.")