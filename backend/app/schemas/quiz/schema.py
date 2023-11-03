from typing import Optional
from pydantic import BaseModel
from core.database.models import User as UserModel
from tortoise.contrib.pydantic import pydantic_model_creator


class User(BaseModel):
    username: str
    email: Optional[str] = None
    password: str

UserIn = pydantic_model_creator(UserModel, name="UserIn", exclude_readonly=True)

UserOut = pydantic_model_creator(
    UserModel, name="UserOut"
)

class Quiz(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    category: str
    difficulty: str
    owner_id: int

class Question(BaseModel):
    id: int
    question_text: str
    options: str
    correct_answer: str
    quiz_id: int

class Answer(BaseModel):
    id: int
    answer: str
    question_id: int
    user_id: int

class Result(BaseModel):
    id: int
    score: int
    time_taken: str
    user_id: int
    quiz_id: int

class Category(BaseModel):
    id: int
    name: str

class Session(BaseModel):
    id: int
    start_time: str
    end_time: str
    user_id: int

class Feedback(BaseModel):
    id: int
    feedback_text: str
    user_id: int

