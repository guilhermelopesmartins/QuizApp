from app.schemas.quiz.schema import Result
from core.repository.base import BaseRepository
from core.database import models

class ResultRepository(BaseRepository[Result]):
    def __init__(self):
        super().__init__(schema=Result, db_model=models.Result)