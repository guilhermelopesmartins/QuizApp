from typing import Any, Generic, Type, TypeVar
from core.exceptions import NotFoundException
from core.repository import BaseRepository

ModelType = TypeVar('ModelType')
class BaseController(Generic[ModelType]):
    """Base class for data controllers."""

    def __init__(self, model: Type[ModelType], repository: BaseRepository):
        self.model_class = model
        self.repository = repository

    async def get_by_id(self, id: int):
        return await self.repository.get_by_id(id)

    async def add(self, entity: ModelType):
        await self.repository.add(entity)

    async def update(self, id: int, entity: ModelType):
        await self.repository.update(id, entity)

    async def delete(self, id: int):
        await self.repository.delete(id)