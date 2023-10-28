from app.schemas.quiz.schema import Question 
from core.repository.base import BaseRepository

class QuestionRepository(BaseRepository[Question]):
    def __init__(self):
        self.entities = {}