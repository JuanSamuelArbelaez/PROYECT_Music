from Model.Structures.ComparableValue.ComparableValue import ComparableValue


class Album(ComparableValue):
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year

    def __lt__(self, other: 'Album') -> bool:
        return self.name < other.name

    def __gt__(self, other: 'Album') -> bool:
        return self.name > other.name

    def __eq__(self, other: 'Album') -> bool:
        return self.name == other.name

    def __le__(self, other: 'Album') -> bool:
        return self.name <= other.name

    def __ge__(self, other: 'Album') -> bool:
        return self.name >= other.name
