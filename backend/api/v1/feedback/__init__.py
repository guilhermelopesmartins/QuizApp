from fastapi import APIRouter

from .feedback import feedback_router

feedback_router = APIRouter()
feedback_router.include_router(feedback_router, prefix="/feedback", tags=["Feedback"])

__all__ = ["feedback_router"]
