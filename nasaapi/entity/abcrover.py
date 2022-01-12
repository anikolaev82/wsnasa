from abc import ABC
from typing import List

from nasaapi.entity.manifest import Photo, Photos, Manifest
from nasaapi.entity.storage import Storage
from nasaapi.utils.repo import Repo


class ABCRover(ABC):
    """
    Родительский класс марсохода
    """

    def __init__(self, rover: str):
        self.__name = rover
        self.__cache = Storage()
        self.__manifest = Repo.manifest(self.__name)

    def manifest(self) -> Manifest:
        return self.__manifest

    def photos(self, days: Photos) -> List[Photo]:
        """
        Возвращает массив классов Photo за выбранный день
        """
        if self.__cache.get(days) is None:
            self.__cache.set(days, Repo.photos(self.__manifest, days))
        return self.__cache.get(days)

    def __str__(self) -> str:
        return self.__name
