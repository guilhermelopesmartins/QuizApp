from fastapi import APIRouter, Depends, HTTPException
from app.controllers import SessionController  # Import the SessionController
from app.schemas.quiz.schema import Session as SessionSchema  # Import the SessionSchema
from typing import List
from core.factory import Factory

session_router = APIRouter()

@session_router.get("/", response_model=List[SessionSchema])
async def get_all_sessions(controller: SessionController = Depends(Factory().get_session_controller)):  # Use the SessionController
    return await controller.repository.get_all()

@session_router.get("/{id}", response_model=SessionSchema)
async def get_session(id: int, controller: SessionController = Depends(Factory().get_session_controller)):  # Use the SessionController
    session = await controller.get_by_id(id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@session_router.post("/", response_model=SessionSchema)
async def create_session(session: SessionSchema, controller: SessionController = Depends(Factory().get_session_controller)):  # Use the SessionController
    return await controller.add(session)

@session_router.put("/{id}", response_model=SessionSchema)
async def update_session(id: int, session: SessionSchema, controller: SessionController = Depends(Factory().get_session_controller)):  # Use the SessionController
    return await controller.update(id, session)

@session_router.delete("/{id}")
async def delete_session(id: int, controller: SessionController = Depends(Factory().get_session_controller)):  # Use the SessionController
    await controller.delete(id)
    return {"message": "Session deleted successfully"}
