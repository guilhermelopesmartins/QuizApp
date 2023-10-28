from fastapi import APIRouter, Depends, HTTPException
from app.controllers import CategoryController  # Import the CategoryController
from app.schemas.quiz.schema import Category as CategorySchema  # Import the CategorySchema
from typing import List
from core.factory import Factory

category_router = APIRouter()

@category_router.get("/", response_model=List[CategorySchema])
async def get_all_categories(controller: CategoryController = Depends(Factory().get_category_controller)):  # Use the CategoryController
    return await controller.repository.get_all()

@category_router.get("/{id}", response_model=CategorySchema)
async def get_category(id: int, controller: CategoryController = Depends(Factory().get_category_controller)):  # Use the CategoryController
    category = await controller.get_by_id(id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@category_router.post("/", response_model=CategorySchema)
async def create_category(category: CategorySchema, controller: CategoryController = Depends(Factory().get_category_controller)):  # Use the CategoryController
    return await controller.add(category)

@category_router.put("/{id}", response_model=CategorySchema)
async def update_category(id: int, category: CategorySchema, controller: CategoryController = Depends(Factory().get_category_controller)):  # Use the CategoryController
    return await controller.update(id, category)

@category_router.delete("/{id}")
async def delete_category(id: int, controller: CategoryController = Depends(Factory().get_category_controller)):  # Use the CategoryController
    await controller.delete(id)
    return {"message": "Category deleted successfully"}
