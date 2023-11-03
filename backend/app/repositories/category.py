from app.schemas.quiz.schema import Category
from core.repository.base import BaseRepository
from core.database import models

class CategoryRepository(BaseRepository[Category]):
    def __init__(self):
        super().__init__(schema=Category, db_model=models.Category)