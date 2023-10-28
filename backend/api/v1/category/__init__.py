from fastapi import APIRouter

from .category import category_router

category_router = APIRouter()
category_router.include_router(category_router, prefix="/category", tags=["Category"])


__all__ = ["category_router"]
