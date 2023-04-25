from Model.Structures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList
from Model.Structures.LinkedList.LinkedList import LinkedList


class Artist:
    def __init__(self, code, name, country, is_group):
        self.__code = code
        self.__name = name
        self.__country = country
        self.__is_group = is_group
        self.__song_list = DoubleLinkedList()
        self.__albums = LinkedList()
        self.__albums.addAll("Singles")

    def add_song(self, song):
        if not self.__albums.contains(song.get_album()):
            raise AttributeError
        else:
            self.__song_list.append(song)



