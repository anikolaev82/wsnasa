from dataclasses import dataclass, field
from datetime import date
from typing import List, Callable


@dataclass
class Photo:
    repo: Callable
    id: int
    img_src: str
    rover: str = field(default=None)
    earth_date: date = field(default=None)
    sol: int = field(default=0)
    camera: dict = field(default_factory=dict)

    def download(self):
        repo = self.repo(self)
        return repo.get_data()


@dataclass
class Photos:
    sol: int = field(default=1)
    earth_date: date = field(default=None)
    total_photos: int = field(default=0)
    cameras: List[str] = field(default_factory=list)

    def __hash__(self):
        return hash(f"{self.sol}-{self.earth_date}-{self.total_photos}-{len(self.cameras)}")


@dataclass
class Manifest:
    name: str
    landing_date: date = field(default=None)
    launch_date: date = field(default=None)
    status: str = field(default=None)
    max_date: date = field(default=None)
    max_sol: int = field(default=0)
    total_photos: int = field(default=0)
    photos: List = field(default_factory=list)
