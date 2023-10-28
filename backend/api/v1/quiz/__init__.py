from fastapi import APIRouter

from .quiz import quiz_router

quiz_router = APIRouter()
quiz_router.include_router(quiz_router, prefix="/quiz", tags=["Quiz"])

__all__ = ["quiz_router"]
