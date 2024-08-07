from datetime import datetime, time
from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.entries import Entry, UpdateBaseEntry

router=APIRouter()

@router.post("/", response_description="Create a new entry", status_code=status.HTTP_201_CREATED, response_model=Entry)
def create_entry(request: Request, entry: Entry = Body(...)):
    entry = jsonable_encoder(entry)
    new_entry = request.app.database["entries"].insert_one(entry)
    created_entry = request.app.database["entries"].find_one(
        {"_id": new_entry.inserted_id}
    )

    return created_entry

@router.get("/", response_description="List all entries", response_model=List[Entry])
def list_all_entries(request: Request):
    entries = list(request.app.database["entries"].find(limit=100))
    return entries

@router.get("/daily", response_description="Show today's entries", response_model=List[Entry])
def list_daily_entries(request: Request):
    time_now = datetime.now()
    start_of_day = datetime.combine(time_now, time.min)
    iso_start_of_day = start_of_day.isoformat()
    end_of_day = datetime.combine(time_now, time.max)
    iso_end_of_day = end_of_day.isoformat()

    entries = list(request.app.database["entries"].find({
        "date": {
            "$gte": iso_start_of_day,
            "$lt": iso_end_of_day
        }
    }))
    return entries

@router.get("/{id}", response_description="Get a single entry by id", response_model=Entry)
def find_entry(id: str, request: Request):
    if (entry := request.app.database["entries"].find_one({"_id": id})) is not None:
        return entry
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entry with ID {id} not found.")

@router.put("/{id}", response_description="Update an entry", response_model=Entry)
def update_entry(id: str, request: Request, entry: UpdateBaseEntry = Body(...)):
    entry = {k: v for k, v in entry.model_dump().items() if v is not None}
    if len(entry) >= 1:
        update_result = request.app.database["entries"].update_one(
            {"_id": id}, {"$set": entry}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entry with ID {id} not found.")
    
    if (
        existing_entry := request.app.database["entries"].find_one({"_id": id})
    ) is not None:
        return existing_entry
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entry with ID {id} not found.")

@router.delete("/{id}", response_description="Delete an entry", response_model=Entry)
def delete_entry(id: str, request: Request, response: Response):
    delete_result = request.app.database["entries"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entry with ID {id} not found.")
