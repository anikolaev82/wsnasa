from abc import ABC
from typing import List

from nasaapi.entity.manifest import Photo, Photos, Manifest
from nasaapi.utils.repo import Repo


class ABCRover(ABC):
    """
    Родительский класс марсохода
    """

    def __init__(self, rover: str):
        self.__name = rover
        self.__manifest = Repo.manifest(self.__name)

    def manifest(self) -> Manifest:
        return self.__manifest

    def photos(self, days: Photos) -> List[Photo]:
        """
        Возвращает массив классов Photo за выбранный день
        """
        return Repo.photos(self.__manifest, days)

    def __str__(self) -> str:
        return self.__name
