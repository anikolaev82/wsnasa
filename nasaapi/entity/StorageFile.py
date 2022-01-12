from .manifest import Photos, Photo
from typing import List, Tuple
import os

class StorageFile:

    def __init__(self):
        self.__path = '{}/{}'
        self.__cache = {}

    def get(self, day: Photos) -> List[Photos]:
        return self.__cache.get(day, None)

    def set(self, day: Photos, data: Tuple[Photo]):
        for i in data:
            print(f'/home/pi/petprojects/nasaapi/nasaapi/Curiosity/{i.id}.jpg')
            with open(f'/home/pi/petprojects/nasaapi/nasaapi/Curiosity/{i.id}.jpg', 'wb') as f:
                f.write(i.download())

