from fastapi import APIRouter, Depends, HTTPException
from app.controllers import QuestionController  # Import the QuestionController
from app.schemas.quiz.schema import Question as QuestionSchema  # Import the QuestionSchema
from typing import List
from core.factory import Factory

question_router = APIRouter()

@question_router.get("/", response_model=List[QuestionSchema])
async def get_all_questions(controller: QuestionController = Depends(Factory().get_question_controller)):  # Use the QuestionController
    return await controller.repository.get_all()

@question_router.get("/{id}", response_model=QuestionSchema)
async def get_question(id: int, controller: QuestionController = Depends(Factory().get_question_controller)):  # Use the QuestionController
    question = await controller.get_by_id(id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@question_router.post("/", response_model=QuestionSchema)
async def create_question(question: QuestionSchema, controller: QuestionController = Depends(Factory().get_question_controller)):  # Use the QuestionController
    return await controller.add(question)

@question_router.put("/{id}", response_model=QuestionSchema)
async def update_question(id: int, question: QuestionSchema, controller: QuestionController = Depends(Factory().get_question_controller)):  # Use the QuestionController
    return await controller.update(id, question)

@question_router.delete("/{id}")
async def delete_question(id: int, controller: QuestionController = Depends(Factory().get_question_controller)):  # Use the QuestionController
    await controller.delete(id)
    return {"message": "Question deleted successfully"}
