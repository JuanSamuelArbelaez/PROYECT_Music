from __future__ import annotations

import string
from Model.Assets.Album.Album import Album
from Model.Structures.ComparableValue.ComparableValue import ComparableValue
from Model.Structures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList
from Model.Structures.LinkedList.LinkedList import LinkedList


class Artist(ComparableValue):
    from Model.Assets.Song import Song

    def __init__(self, code: string, name: string, country: string, is_group: bool):
        self.__code = code
        self.__name = name
        self.__country = country
        self.__is_group = is_group
        self.__song_list = DoubleLinkedList()
        self.__albums = LinkedList[Album]()
        self.__albums.append(Album("Singles", ""))

    def add_song(self, song: Song):
        if self.__song_list.contains(song):
            raise AttributeError("Song already added")
        if not self.__albums.contains(song.get_album()):
            raise AttributeError("Album not found")
        else:
            self.__song_list.append(song)

    def add_album(self, album: Album):
        if self.__albums.contains(album):
            raise AttributeError("Album already added")
        else:
            self.__albums.append(album)

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_name(self):
        return self.__name

    def set_name(self, name: string):
        self.__name = name

    def get_country(self):
        return self.__country

    def set_country(self, country: string):
        self.__country = country

    # Getter and setter for is_group
    def get_is_group(self):
        return self.__is_group

    def set_is_group(self, is_group: bool):
        self.__is_group = is_group

    # Getter and setter for song_list
    def get_song_list(self):
        return self.__song_list

    def set_song_list(self, song_list: DoubleLinkedList[Song]):
        self.__song_list = song_list

    # Getter and setter for albums
    def get_albums(self):
        return self.__albums

    def set_albums(self, albums: LinkedList[Album]):
        self.__albums = albums

    def __lt__(self, other: 'Artist') -> bool:
        return self.__name < other.get_name()

    def __gt__(self, other: 'Artist') -> bool:
        return self.__name > other.get_name()

    def __eq__(self, other: 'Artist') -> bool:
        return self.__name == other.get_name()

    def __le__(self, other: 'Artist') -> bool:
        return self.__name <= other.get_name()

    def __ge__(self, other: 'Artist') -> bool:
        return self.__name >= other.get_name()
