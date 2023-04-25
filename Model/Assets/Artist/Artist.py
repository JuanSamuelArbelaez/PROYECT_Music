from Model.Structures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList


class Artist:
    def __init__(self, code, name, country, is_group):
        self.__code = code
        self.__name = name
        self.__country = country
        self.__is_group = is_group
        self.__song_list = DoubleLinkedList()

