from typing import List, Type


class Column:
    def __init__(self, name: str, nullable: bool = False, unique: bool = False):
        self.name: str = name
        self.nullable: bool = nullable
        self.unique: bool = unique


class CharField(Column):
    def __init__(self, max_length: int = 255, **kwargs):
        self.max_length: int = max_length
        super(CharField, self).__init__(self, **kwargs)


class IntegerField(Column):
    max_length: int = 255


class Migration:
    table_name: str = ''
    columns: List[Type[Column]] = []
