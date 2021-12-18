
class Curiosity:

    def __init__(self):
        self.__name = 'Curiosity'
        self.__cameras = ('FHAZ', 'RHAZ', 'MAST', 'CHEMCAM', 'MAHLI', 'MARDI', 'NAVCAM')

    def get_cameras(self) -> tuple:
        return self.__cameras

    def has_camera(self, camera: str) -> bool:
        return camera in self.__cameras

    def __str__(self) -> str:
        return self.__name
