

class Config:
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._token = kwargs.get('token')
            cls._base_uri = kwargs.get('base_uri')
            cls._instance[cls] = cls
        return cls._instance[cls]

    @classmethod
    def token(cls):
        return cls._token

    @classmethod
    def base_uri(cls):
        return cls._base_uri
