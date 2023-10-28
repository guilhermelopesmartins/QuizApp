from app.schemas.quiz.schema import Quiz
from core.repository.base import BaseRepository

class QuizRepository(BaseRepository[Quiz]):
    def __init__(self):
        self.entities = {}
