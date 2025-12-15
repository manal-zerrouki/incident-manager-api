from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

class IncidentCreate(BaseModel):
    title: str
    severity: int  # 1..5

class Incident(IncidentCreate):
    id: int

_db: Dict[int, Incident] = {}
_next_id = 1

@router.post("", response_model=Incident, status_code=201)
def create_incident(payload: IncidentCreate):
    global _next_id
    incident = Incident(id=_next_id, **payload.model_dump())
    _db[_next_id] = incident
    _next_id += 1
    return incident

@router.get("", response_model=list[Incident])
def list_incidents():
    return list(_db.values())

@router.get("/{incident_id}", response_model=Incident)
def get_incident(incident_id: int):
    if incident_id not in _db:
        raise HTTPException(status_code=404, detail="Incident not found")
    return _db[incident_id]

@router.delete("/{incident_id}", status_code=204)
def delete_incident(incident_id: int):
    if incident_id not in _db:
        raise HTTPException(status_code=404, detail="Incident not found")
    del _db[incident_id]
