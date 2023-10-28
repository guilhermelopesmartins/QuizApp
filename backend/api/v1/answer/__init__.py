from fastapi import APIRouter

from .answer import answer_router

answer_router = APIRouter()
# monitoring_router.include_router(health_router, prefix="/health", tags=["Health"])
answer_router.include_router(answer_router)

__all__ = ["answer_router"]