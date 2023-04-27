import string

from Model.Structures.ComparableValue.ComparableValue import ComparableValue


class Tag(ComparableValue):
    def __init__(self, attribute: string):
        self.__attribute = attribute

    def get_attribute__(self):
        return self.__attribute

    def __lt__(self, other: 'Tag') -> bool:
        return self.__attribute < other.get_attribute__()

    def __gt__(self, other: 'Tag') -> bool:
        return self.__attribute > other.get_attribute__()

    def __eq__(self, other: 'Tag') -> bool:
        return self.__attribute == other.get_attribute__()

    def __le__(self, other: 'Tag') -> bool:
        return self.__attribute <= other.get_attribute__()

    def __ge__(self, other: 'Tag') -> bool:
        return self.__attribute >= other.get_attribute__()
