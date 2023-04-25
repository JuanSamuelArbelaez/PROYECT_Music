from Model.Assets.Cover.Cover import Cover
from Model.Assets.Tag.Tag import Tag
from Model.Structures.LinkedList.LinkedList import LinkedList


class Song:

    def __init__(self, name, id, album, artist, year, duration, genre, url):
        self.__name = name
        self.__id = id
        self.__album = album
        self.__artist = artist
        self.__year = year
        self.__duration = duration
        self.__genre = Tag(genre)
        self.__url = url
        self.__cover = Cover(self.__url, id)
        #self.__audio = Audio(self.__url)
        self.__tags = LinkedList()
        self.__tags.append(self.__genre)
        self.__tags.append(self.__artist)


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_album(self):
        return self.__album

    def set_album(self, album):
        self.__album = album

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = Tag(genre)

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_cover(self):
        return self.__cover

    def set_cover(self, id):
        self.__cover = Cover(self.__url, id)