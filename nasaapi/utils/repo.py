import base64
import json
import math
from abc import ABC, abstractmethod
from typing import Tuple

import requests

from nasaapi.config import Config
from nasaapi.entity.manifest import Manifest, DayOfMars, Photo


class AbcRepo(ABC):
    """
    Абстрактный класс хранилища данных.
    От него наследуются все классы получающие данные
    """

    def __init__(self):
        self._config = Config()
        self._cache = self._config.storage()
        self._base_uri = self._config.base_uri()
        self._token = self._config.token()

    @abstractmethod
    def request(self):
        raise NotImplementedError


class RepoManifest(AbcRepo):
    """
    Получает данные манифеста соответствующего марсохода
    """

    def __init__(self, rover: str):
        super().__init__()
        if len(rover.lstrip().rstrip()) == 0 or rover is None:
            raise Exception("Name rover's can't be None")
        self.__rover = rover
        self.__manifest_uri = f'{self._base_uri}manifests/{self.__rover}'
        self.__keys = {'api_key': self._token}

    def request(self) -> Manifest:
        """
        Возвращает данные либо от вебсервиса либо из кэша
        :return:
        """
        manifest = self._cache.get(self.__rover)
        if manifest is None:
            manifest = requests.get(self.__manifest_uri, params=self.__keys).json()
            self._cache.set(self.__rover, manifest)
            print('requests.get')
        photo_manifest = manifest.get('photo_manifest')
        photos_json = photo_manifest.get('photos')
        photo_manifest['photos'] = [DayOfMars(**photo) for photo in photos_json]
        return Manifest(**photo_manifest)


class RepoBPhoto(AbcRepo):
    """
    Загружает изображение
    """

    def __init__(self, photo: Photo):
        super().__init__()
        self._photo = photo

    def request(self) -> bytes:
        """
        Получает изображение и возвращает бинарный объект
        :return:
        """
        photo = self._cache.get(self._photo)
        if photo is None:
            photo = requests.get(self._photo.img_src).content
            self._cache.set(self._photo, photo)
        else:
            photo = bytes(base64.b64decode(json.loads(photo)['img']))
        return photo


class RepoPhoto(AbcRepo):
    """
    Получает полный список ссылок и метаданных по существующим фотографиям
    """

    def __init__(self, rover: Manifest, day: DayOfMars):
        super().__init__()
        self.__rover = rover
        self.__day = day
        self._key = (self.__rover, self.__day)
        self.__page_size = 25  # константа. Лимит на выдачу от api
        try:
            self.__page_count = int(math.ceil(self.__day.total_photos / self.__page_size)) + 1
        except ValueError:
            self.__page_count = 1
        self.__base_uri = f'{self._base_uri}/rovers/{rover.name}/photos'
        self.__keys = {'sol': day.sol, 'page': 1, 'api_key': self._token}

    def request(self) -> Tuple:
        """
        Получает данные из вебсервиса или кэша список фотографиц за
        выбранный день
        """
        ret = self._cache.get(self._key)
        if ret is None:
            ret = []
            for i in range(1, self.__page_count):
                self.__keys['page'] = i
                response = requests.get(self.__base_uri, params=self.__keys).json()
                ret.extend(response['photos'])

            self._cache.set(self._key, ret)
        return tuple(Photo(RepoBPhoto, **i) for i in ret)


class Repo:
    @staticmethod
    def manifest(rover: str) -> Manifest:
        manifest = RepoManifest(rover)
        return manifest.request()

    @staticmethod
    def photos(rover: Manifest, day: DayOfMars) -> Tuple[Photo]:
        return RepoPhoto(rover, day).request()
