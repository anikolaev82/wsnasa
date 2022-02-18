import datetime
import random
from nasaapi.utils.repo import Repo


class AbcAPOD:

    def __init__(self):
        self._start_date = datetime.date(year=1995, month=6, day=16)  #ограничение сервиса
        self._end_date = datetime.date.today()
        self._repo = Repo.apod

    def get_random(self):
        rand = random.randint(1, abs((self._end_date - self._start_date).days))
        rand_day = self._start_date + datetime.timedelta(days=rand)
        return self._repo(rand_day)

    def get_today(self):
        return self._repo(datetime.date.today())

    def __str__(self) -> str:
        return self.__name
