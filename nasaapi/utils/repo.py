import json
import math
from abc import ABC, abstractmethod
from typing import Iterable, Tuple

import requests

from nasaapi.config import BASE_URI, TOKEN
from nasaapi.entity.manifest import Manifest, Photos, Photo


class AbcRepo(ABC):
    """
    Абстрактный класс хранилища данных.
    От него наследуются все классы получающие данные
    """
    def __init__(self):
        self._base_uri = BASE_URI
        self._token = TOKEN

    @abstractmethod
    def get_data(self):
        raise NotImplementedError


class RepoManifest(AbcRepo):

    def __init__(self, rover: str):
        super().__init__()
        if len(rover.lstrip().rstrip()) == 0 or rover is None:
            raise Exception("Name rover's can't be None")
        self.__rover = rover
        self.__manifest_uri = f'{self._base_uri}manifests/{self.__rover}'
        self.__keys = {'api_key': self._token}
        self.__data = {}

    def get_data(self):
        if self.__data.get(self.__rover, None) is None:
            print(self.__manifest_uri)
            manifest = requests.get(self.__manifest_uri, params=self.__keys).json()
            photo_manifest = manifest.get('photo_manifest')
            photos_json = photo_manifest.get('photos')
            photo_manifest['photos'] = [Photos(**photo) for photo in photos_json]
            self.__rover = photo_manifest['name']
            self.__data.setdefault(self.__rover, Manifest(**photo_manifest))
        return self.__data.get(self.__rover)


class RepoBPhoto(AbcRepo):

    def __init__(self, photo: Photo):
        super().__init__()
        self._photo = photo
        self._img = None

    def get_data(self):
        if self._img is None:
            self._img = requests.get(self._photo.img_src).content
        return self._img


class RepoPhoto(AbcRepo):

    def __init__(self, rover: Manifest, day: Photos):
        super().__init__()
        self.__rover = rover
        self.__day = day
        self.__page_size = 25
        try:
            self.__page_count = int(math.ceil(self.__day.total_photos / self.__page_size)) + 1
        except ValueError:
            self.__page_count = 1
        self.__reciv = []
        self.__raw_data = None
        self.__base_uri = f'{self._base_uri}/rovers/{rover.name}/photos'
        self.__keys = {'sol': day.sol, 'page': 1, 'api_key': self._token}

    def get_data(self):
        if isinstance(self.__reciv, Iterable) and len(self.__reciv) == 0:
            for i in range(1, self.__page_count):
                self.__keys['page'] = i
                response = requests.get(self.__base_uri, params=self.__keys)
                self.__raw_data = json.loads(response.content)['photos']
                self.__reciv.extend(tuple(Photo(RepoBPhoto, **i) for i in self.__raw_data))
        return self.__reciv


class Repo:

    @staticmethod
    def manifest(rover: str) -> Manifest:
        manifest = RepoManifest(rover)
        return manifest.get_data()

    @staticmethod
    def photos(rover: Manifest, day: Photos) -> Tuple[Photo]:
        return RepoPhoto(rover, day).get_data()
