from fastapi import APIRouter, Depends, HTTPException
from app.controllers import QuizController  # Import the QuizController
from app.schemas.quiz.schema import Quiz as QuizSchema  # Import the QuizSchema
from typing import List
from core.factory import Factory

quiz_router = APIRouter()

@quiz_router.get("/", response_model=List[QuizSchema])
async def get_all_quizzes(controller: QuizController = Depends(Factory().get_quiz_controller)):  # Use the QuizController
    return await controller.repository.get_all()

@quiz_router.get("/{id}", response_model=QuizSchema)
async def get_quiz(id: int, controller: QuizController = Depends(Factory().get_quiz_controller)):  # Use the QuizController
    quiz = await controller.get_by_id(id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@quiz_router.post("/", response_model=QuizSchema)
async def create_quiz(quiz: QuizSchema, controller: QuizController = Depends(Factory().get_quiz_controller)):  # Use the QuizController
    return await controller.add(quiz)

@quiz_router.put("/{id}", response_model=QuizSchema)
async def update_quiz(id: int, quiz: QuizSchema, controller: QuizController = Depends(Factory().get_quiz_controller)):  # Use the QuizController
    return await controller.update(id, quiz)

@quiz_router.delete("/{id}")
async def delete_quiz(id: int, controller: QuizController = Depends(Factory().get_quiz_controller)):  # Use the QuizController
    await controller.delete(id)
    return {"message": "Quiz deleted successfully"}
