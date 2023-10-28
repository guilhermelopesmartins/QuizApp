from app.schemas.quiz.schema import Feedback
from core.repository.base import BaseRepository

class FeedbackRepository(BaseRepository[Feedback]):
    def __init__(self):
        self.entities = {}