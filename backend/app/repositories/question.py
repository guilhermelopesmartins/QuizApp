from app.schemas.quiz.schema import Question
from core.repository.base import BaseRepository
from core.database import models

class QuestionRepository(BaseRepository[Question]):
    def __init__(self):
        super().__init__(schema=Question, db_model=models.Question)