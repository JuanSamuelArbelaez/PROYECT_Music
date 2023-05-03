from Model.Structures.ComparableValue.ComparableValue import ComparableValue


class Tag(ComparableValue):
    def __init__(self, attribute: str):
        self.__attribute = attribute

    def get_attribute(self):
        return self.__attribute

    def __lt__(self, other: 'Tag') -> bool:
        return self.__attribute < other.get_attribute()

    def __gt__(self, other: 'Tag') -> bool:
        return self.__attribute > other.get_attribute()

    def __eq__(self, other: 'Tag') -> bool:
        return self.__attribute == other.get_attribute()

    def __le__(self, other: 'Tag') -> bool:
        return self.__attribute <= other.get_attribute()

    def __ge__(self, other: 'Tag') -> bool:
        return self.__attribute >= other.get_attribute()

    def get_compatibility(self, tag2: 'Tag') -> bool:
        if not self or not tag2:
            raise ValueError("String can't be null")
        if len(self.__attribute) == 0 or len(tag2.get_attribute()) == 0:
            raise ValueError('Both strings must have length above 0')

        string1 = self.__attribute.lower()
        string2 = tag2.get_attribute().lower()

        if string1 == string2:
            return True

        if string1 in string2 or string2 in string1:
            return True

        return False
