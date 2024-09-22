from abc import ABC, abstractmethod

class CacheRepository(ABC):

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def get(self, key: str):
        pass
    
    @abstractmethod
    async def set(self, value: str):
        pass
    
    @abstractmethod
    async def close(self):
        pass
