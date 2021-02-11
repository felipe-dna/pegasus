import sqlite3
from sqlite3 import Error


def create_connection(path: str):
    connection = None

    try:
        connection = sqlite3.connect(path)
    except Error as error:
        print(error)
    finally:
        if connection:
            connection.close()
