#from nasaapi.entity.storagememory import StorageMemory
from typing import Any


class Config:
    """
    Хранит необходимые настройки
    """
    __instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__token = kwargs.get('token')
            cls.__base_uri = kwargs.get('base_uri')
            cls.__connection_string = kwargs.get('connection_string', None)
            cls.__storage = kwargs.get('storage')
            cls.__instance[cls] = cls
        return cls.__instance[cls]

    @classmethod
    def token(cls) -> str:
        return cls.__token

    @classmethod
    def base_uri(cls) -> str:
        return cls.__base_uri

    @classmethod
    def connection_string(cls) -> str:
        return cls.__connection_string

    @classmethod
    def storage(cls)  -> Any:
        return cls.__storage()
