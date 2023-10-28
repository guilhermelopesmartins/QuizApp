from fastapi import APIRouter

from .monitoring import monitoring_router
from .answer import answer_router
from .category import category_router
from .feedback import feedback_router
from .question import question_router
from .quiz import quiz_router
from .result import result_router
from .session import session_router


v1_router = APIRouter()
v1_router.include_router(monitoring_router, prefix="/monitoring")
v1_router.include_router(answer_router, prefix="/sdfsfs")
v1_router.include_router(category_router, prefix="/category")
v1_router.include_router(feedback_router, prefix="/feedback")
v1_router.include_router(question_router, prefix="/question")
v1_router.include_router(quiz_router, prefix="/quiz")
v1_router.include_router(result_router, prefix="/result")
v1_router.include_router(session_router, prefix="/session")


