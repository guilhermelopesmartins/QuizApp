from fastapi import APIRouter

from .result import result_router

results_router = APIRouter()
results_router.include_router(result_router, prefix="/result", tags=["Users"])

__all__ = ["results_router"]
