from fastapi import APIRouter

from .session import session_router

session_router = APIRouter()
session_router.include_router(session_router, prefix="/session", tags=["Session"])

__all__ = ["session_router"]
