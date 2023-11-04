from app.schemas.quiz.schema import Quiz
from core.repository.base import BaseRepository
from core.database import models

class QuizRepository(BaseRepository[Quiz]):
    def __init__(self):
        super().__init__(schema=Quiz, db_model=models.Quiz)