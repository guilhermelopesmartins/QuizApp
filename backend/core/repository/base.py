from typing import TypeVar, Dict, Generic

EntityType = TypeVar('EntityType')

class BaseRepository(Generic[EntityType]):
    def __init__(self):
        self.entities = Dict[str, EntityType]()

    def get_by_key(self, key: str):
        return self.entities.get(key)

    def add_entity(self, entity: EntityType, key: str):
        self.entities[key] = entity

    def update_entity(self, key: str, updated_entity: EntityType):
        if key in self.entities:
            self.entities[key] = updated_entity

    def delete_entity(self, key: str):
        if key in self.entities:
            del self.entities[key]
