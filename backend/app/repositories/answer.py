from app.schemas.quiz.schema import Answer
from core.repository.base import BaseRepository
from core.database import models

class AnswerRepository(BaseRepository[Answer]):
    def __init__(self):
        super().__init__(schema=Answer, db_model=models.Answer)