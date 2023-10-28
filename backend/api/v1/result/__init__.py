from fastapi import APIRouter

from .result import result_router

result_router = APIRouter()
result_router.include_router(result_router, prefix="/result", tags=["Users"])

__all__ = ["result_router"]
