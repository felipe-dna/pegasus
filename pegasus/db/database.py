from typing import Optional

from pegasus.db.drivers import Sqlite


class Drivers:
    SQlite3 = 'sqlite3'


class DatabaseConfig:
    def __init__(
            self,
            name: str,
            base_path: Optional[str]
    ) -> None:
        self.name = name
        self.base_path = base_path


class Database:
    VALID_TYPES = Drivers.__dict__.values()

    def __init__(
            self,
            type: str,
            config: DatabaseConfig
    ) -> None:
        if type not in self.VALID_TYPES:
            raise NotImplementedError(
                f'Theres not support to {type} databases yet.'
            )

        if type == Drivers.SQlite3:
            self.db = Sqlite(
                file_name=f'{config.base_path}/{config.name}.sqlite3'
            )
