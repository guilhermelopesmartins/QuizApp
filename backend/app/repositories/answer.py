from app.schemas.quiz.schema import Answer
from core.repository.base import BaseRepository


class AnswerRepository(BaseRepository[Answer]):
    def __init__(self):
        self.entities = {}