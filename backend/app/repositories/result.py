from app.schemas.quiz.schema import Result
from core.repository.base import BaseRepository

class ResultRepository(BaseRepository[Result]):
    def __init__(self):
        self.entities = {}
