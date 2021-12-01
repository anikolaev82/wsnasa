

class Curiosity:

    def __init__(self):
        self.__name = 'Curiosity'
        self.__cameras = ('FHAZ', 'RHAZ', 'MAST', 'CHEMCAM', 'MAHLI', 'MARDI', 'NAVCAM')

    def get_cameras(self):
        return self.__cameras

    def has_camera(self, camera: str):
        return self.__cameras in camera

    def __str__(self):
        return self.__name
