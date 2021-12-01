from entity.manifest import Photos
from typing import Iterable
from utils.repo import Repo


class Spirit:

    def __init__(self):
        self.__name = 'Spirit'
        self.__manifest = Repo.manifest(self.__name)
        self.__photos = None

    def manifest(self):
        return self.__manifest

    def photos(self, days: Photos):
        if self.__photos is None:
            self.__photos = Repo.photos(self.__manifest, days)
        return self.__photos

    def __str__(self):
        return self.__name
