import sqlite3
from sqlite3 import Error

from pegasus.cli.logs import log


class BaseDriver:
    @staticmethod
    def error(message: str) -> None:
        log(message, "red")

    def get_connection(self, *args, **kwargs):
        ...


class Sqlite(BaseDriver):
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name
        self.__db = None
        self.init_database()

    def get_connection(self):
        try:
            self.__db = sqlite3.connect(self.file_name)
        except Error as error:
            self.error(error)
        else:
            return self.__db

    def close_connection(self):
        self.__db.close() if self.__db else ...

    def init_database(self):
        self.get_connection()
        self.close_connection()
