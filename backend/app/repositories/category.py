from app.schemas.quiz.schema import Category
from core.repository.base import BaseRepository


class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        self.entities = {}