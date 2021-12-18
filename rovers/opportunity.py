
class Curiosity:

    def __init__(self):
        self.__name = 'Opportunity'
        self.__cameras = ('FHAZ', 'RHAZ', 'NAVCAM', 'PANCAM', 'MINITES')

    def get_cameras(self) -> tuple:
        return self.__cameras

    def has_camera(self, camera: str) -> bool:
        return camera in self.__cameras

    def __str__(self) -> str:
        return self.__name
