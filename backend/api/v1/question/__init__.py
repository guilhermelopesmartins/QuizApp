from fastapi import APIRouter

from .question import question_router

question_router = APIRouter()
question_router.include_router(question_router, prefix="/question", tags=["Question"])

__all__ = ["question_router"]
