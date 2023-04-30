import string

from Model.Structures.ComparableValue.ComparableValue import ComparableValue


class Tag(ComparableValue):
    def __init__(self, attribute: str):
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

    def get_compatibility(self, attribute: str):
        if type(attribute) != 'str' or len(attribute)<=0 :
            raise AttributeError("Not comparable")
        else:
            att1_low = self.__attribute.lower()
            att2_low = attribute.lower()
            if (att2_low in att1_low) or (att1_low in att2_low):
                short = min(len(att1_low), len(att2_low))
                return 1.1 - (1/short)
