import io
from dataclasses import dataclass, field, asdict
from datetime import date
from typing import List, Callable, Any
import json
import base64
from nasaapi.utils.makeuuid import MakeUUID


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
        return repo.request()

    def uuid(self):
        return MakeUUID.make(f'{self.id}-{self.img_src}-{self.earth_date}')

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    def __hash__(self):
        return hash(self.uuid())


@dataclass
class Photos:
    sol: int = field(default=1)
    earth_date: date = field(default=None)
    total_photos: int = field(default=0)
    cameras: List[str] = field(default_factory=list)

    def uuid(self):
        return MakeUUID.make(f"Photos{self.sol}-{self.earth_date}-{self.total_photos}-{len(self.cameras)}")

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    def __hash__(self):
        return hash(self.uuid())


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

    def uuid(self):
        return MakeUUID.make(f'{self.name}-{self.launch_date}-{self.max_sol}')

    def __hash__(self):
        return hash(self.uuid())

    def to_json(self) -> str:
        return json.dumps(asdict(self))


class ObjectEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, bytes):
            print('bytes')
            o_base64_encode = base64.b64encode(o)
            o_decode = o_base64_encode.decode('utf8')
            o_str = json.dumps({'img': f'{o_decode}'})
            return o_str
        else:
            print('not bytes')
            return o.__dict__
