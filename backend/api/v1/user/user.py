from fastapi import APIRouter, Depends, HTTPException
from app.controllers import UserController  # Import the UserController
from app.schemas.quiz.schema import User as UserSchema  # Import the UserSchema
from typing import List
from core.factory import Factory

user_router = APIRouter()

@user_router.get("/", response_model=List[UserSchema])
async def get_all_users(controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    return await controller.repository.get_all()

@user_router.get("/{id}", response_model=UserSchema)
async def get_user(id: int, controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    user = await controller.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.post("/", response_model=UserSchema)
async def create_user(user: UserSchema, controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    return await controller.add(user)

@user_router.put("/{id}", response_model=UserSchema)
async def update_user(id: int, user: UserSchema, controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    return await controller.update(id, user)

@user_router.delete("/{id}")
async def delete_user(id: int, controller: UserController = Depends(Factory().get_user_controller)):  # Use the UserController
    await controller.delete(id)
    return {"message": "User deleted successfully"}
