from .manifest import Photos, Photo
from typing import List, Tuple

from nasaapi.entity.abc.abcstorage import AbcStorage


class StorageMemory(AbcStorage):

    def __init__(self):
        super().__init__()
        self.__cache = {}

    def get(self, day: Photos) -> List[Photos]:
        return self.__cache.get(day, None)

    def set(self, day: Photos, data: Tuple[Photo]):
        self.__cache.setdefault(day, data)
