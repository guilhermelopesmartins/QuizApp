from app.schemas.quiz.schema import Feedback
from core.repository.base import BaseRepository
from core.database import models

class FeedbackRepository(BaseRepository[Feedback]):
    def __init__(self):
        super().__init__(schema=Feedback, db_model=models.Feedback)