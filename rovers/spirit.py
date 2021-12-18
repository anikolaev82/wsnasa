from entity.manifest import Photo, Photos, Manifest
from typing import List
from utils.repo import Repo, RepoBPhoto


class Spirit:

    def __init__(self):
        self.__name = 'Spirit'
        self.__manifest = Repo.manifest(self.__name)
        self.__photos = None

    def manifest(self) -> Manifest:
        return self.__manifest

    def photos(self, days: Photos) -> List[Photo]:
        if self.__photos is None:
            self.__photos = Repo.photos(self.__manifest, days)
        return self.__photos

    def __str__(self) -> str:
        return self.__name
