import json

from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from nasaapi.utils.makeuuid import MakeUUID
from nasaapi.entity.abc.abcstorage import AbcStorage
from .manifest import ObjectEncoder

from typing import Hashable, Any

Base = declarative_base()


class ModelKeyValue(Base):
    __tablename__ = 'nasaapi_keyvalue'

    key = Column(String, primary_key=True, nullable=False)
    value = Column(JSON, nullable=False)


class StorageDatabase(AbcStorage):

    def __init__(self):
        super().__init__()
        self._connection_string = self._config.connection_string()
        self._engine = create_engine(self._connection_string)
        self._session = scoped_session(sessionmaker(autocommit=False, bind=self._engine))
        Base.metadata.create_all(bind=self._engine)

    def get(self, key: Hashable) -> Any:
        s = select(ModelKeyValue).where(ModelKeyValue.key == f"{MakeUUID.make(key)}")
        ret = None
        with self._engine.connect() as conn:
            for row in conn.execute(s).all():
                ret = json.loads(row.value)
        return ret

    def set(self, key: Hashable, value: str):
        object_encoder = ObjectEncoder()
        obj_json = object_encoder.encode(value)
        tbl = ModelKeyValue(key=MakeUUID.make(key), value=obj_json)
        self._session.add(tbl)
        self._session.commit()

    def __del__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
