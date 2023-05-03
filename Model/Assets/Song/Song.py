from __future__ import annotations

import os

from Model.Assets.Album import Album
from Model.Assets.Cover.Cover import Cover
from Model.Assets.Tag.Tag import Tag
from Model.Structures.BinaryTree.BinaryTree import BinaryTree
from Model.Structures.ComparableValue.ComparableValue import ComparableValue
from Model.Tools.FileManager.FileManager import retrieve_audio


class Song(ComparableValue):

    def __init__(self, name: str, code: str, album: Album, artist, year: str, duration: int,
                 genre: str, url: str):

        self.__name = name
        self.__id = code
        self.__album = album
        self.__artist = artist
        self.__year = year
        self.__duration = duration
        self.__genre = Tag(genre)
        self.__url = url

        path = os.path.join(os.path.join(os.getcwd(), "Model"), "Files")

        self.__cover = Cover(code, self.__url, path)
        # self.__audio = retrieve_audio(code, self.__url, path)
        self.__tags = BinaryTree[Tag]()
        self.__tags.add(self.__genre)
        self.__tags.add(Tag(self.__artist.get_name()))
        self.__tags.add(Tag(album.name))
        self.__tags.balance()

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, code: str):
        self.__id = code

    def get_album(self):
        return self.__album

    def set_album(self, album: Album):
        self.__album = album

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist

    def get_year(self):
        return self.__year

    def set_year(self, year: str):
        self.__year = year

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration: int):
        self.__duration = duration

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre: str):
        self.__genre = Tag(genre)

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_cover(self):
        return self.__cover

    def set_cover(self, code: str):
        self.__cover = Cover(self.__url, code)

    def get_all_tags(self) -> []:
        return self.__tags.in_order_traversal()

    def get_filtered_tags(self, tag: Tag) -> []:
        values = []
        for aux_tag in self.get_all_tags():
            if tag.get_compatibility(aux_tag):
                values.append(aux_tag)
        return values

    def add_tag(self, tag: Tag):
        if self.__tags.contains(tag):
            raise AttributeError("Song already has this tag")
        else:
            self.__tags.add(tag)
            self.__tags.balance()

    def remove_tag(self, tag: Tag):
        self.__tags.remove(tag)

    def contains_true_tag(self, tag: Tag) -> bool:
        return self.__tags.contains(tag)

    def contains_partial_tag(self, tag: Tag) -> bool:
        for aux_tag in self.get_all_tags():
            if tag.get_compatibility(aux_tag):
                return True
        return False

    def __lt__(self, other: 'Song') -> bool:
        return self.__id < other.get_id()

    def __gt__(self, other: 'Song') -> bool:
        return self.__id > other.get_id()

    def __eq__(self, other: 'Song') -> bool:
        return self.__id == other.get_id()

    def __le__(self, other: 'Song') -> bool:
        return self.__id <= other.get_id()

    def __ge__(self, other: 'Song') -> bool:
        return self.__id >= other.get_id()
