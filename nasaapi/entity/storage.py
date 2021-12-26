from .manifest import Photos, Photo
from typing import List, Tuple


class Storage:

    def __init__(self):
        self.__cache = {}

    def get(self, day: Photos) -> List[Photos]:
        return self.__cache.get(day, None)

    def set(self, day: Photos, data: Tuple[Photo]):
        self.__cache.setdefault(day, data)
