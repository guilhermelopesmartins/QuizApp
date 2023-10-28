from fastapi import APIRouter, Depends, HTTPException
from app.controllers import FeedbackController  # Import the FeedbackController
from app.schemas.quiz.schema import Feedback as FeedbackSchema  # Import the FeedbackSchema
from typing import List
from core.factory import Factory

feedback_router = APIRouter()

@feedback_router.get("/", response_model=List[FeedbackSchema])
async def get_all_feedbacks(controller: FeedbackController = Depends(Factory().get_feedback_controller)):  # Use the FeedbackController
    return await controller.repository.get_all()

@feedback_router.get("/{id}", response_model=FeedbackSchema)
async def get_feedback(id: int, controller: FeedbackController = Depends(Factory().get_feedback_controller)):  # Use the FeedbackController
    feedback = await controller.get_by_id(id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return feedback

@feedback_router.post("/", response_model=FeedbackSchema)
async def create_feedback(feedback: FeedbackSchema, controller: FeedbackController = Depends(Factory().get_feedback_controller)):  # Use the FeedbackController
    return await controller.add(feedback)

@feedback_router.put("/{id}", response_model=FeedbackSchema)
async def update_feedback(id: int, feedback: FeedbackSchema, controller: FeedbackController = Depends(Factory().get_feedback_controller)):  # Use the FeedbackController
    return await controller.update(id, feedback)

@feedback_router.delete("/{id}")
async def delete_feedback(id: int, controller: FeedbackController = Depends(Factory().get_feedback_controller)):  # Use the FeedbackController
    await controller.delete(id)
    return {"message": "Feedback deleted successfully"}
