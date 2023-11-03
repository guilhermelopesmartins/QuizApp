from typing import TypeVar, Dict, Generic

EntityType = TypeVar('EntityType')

import asyncio

async def main():
    await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

class BaseRepository(Generic[EntityType]):
    def __init__(self):
        self.entities = {}
        # Dict[str, EntityType]

    async def get_all(self):
        return self.entities

    async def get_by_id(self, key: str):
        return self.entities.get(key)

    async def add_entity(self, entity: EntityType, key: str):
        self.entities[key] = entity

    async def update_entity(self, key: str, updated_entity: EntityType):
        if key in self.entities:
            self.entities[key] = updated_entity

    async def delete_entity(self, key: str):
        if key in self.entities:
            del self.entities[key]
