from app.schemas.quiz.schema import Session
from core.repository.base import BaseRepository


class SessionRepository(BaseRepository[Session]):
    def __init__(self):
        self.entities = {}
