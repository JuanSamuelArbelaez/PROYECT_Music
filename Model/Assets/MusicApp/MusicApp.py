import os
import pickle
import string

from Model.Assets.Admin.Admin import Admin
from Model.Assets.Artist import Artist
from Model.Assets.Song import Song
from Model.Assets.User import User
from Model.Structures.BinaryTree.BinaryTree import BinaryTree
from Model.Structures.HashMap.HashMap import HashMap
from Model.Structures.LinkedList.LinkedList import LinkedList


class MusicApp:
    def __init__(self, file_path):
        # Replace serialization on path to serialization on cloud

        self.file_path = file_path

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                loaded = pickle.load(file)
                self.__dict__.update(loaded.__dict__)
        else:
            self.__artist = BinaryTree()
            self.__songs = LinkedList()
            self.__users = HashMap()
            self.__admin = Admin("Robin", "0todos", "robin@musicapp.com")
            self.save()
            pass

    def save(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self, file)

    def add__song(self, song: Song):
        if song is None:
            raise AttributeError("Song can't be None")
        if song.get_artist() is None:
            raise AttributeError("Artist can't be None")
        if not self.__artist.contains(song.get_artist()):
            raise AttributeError("Artist not found")
        else:
            song.get_artist().add_song(song)
            self.__songs.append(song)

    def add__artist(self, artist: Artist):
        self.__artist.add(artist)
        self.__artist.balance()

    def add__user(self, user: User):
        self.__users.put(user.get_username(), user)

    def add_song_tag(self, song: Song, tag: string):
        if song.contains_tag(tag):
            raise AttributeError("Tag already assigned here")
        else:
            song.add_tag(tag)

    def remove_song_tag(self, song: Song, tag: string):
        if not song.contains_tag(tag):
            raise AttributeError("Unable to delete tab not assigned")
        else:
            song.remove_tag(tag)

    def remove_song(self, song: Song):
        if not self.__songs.contains(song):
            raise AttributeError("Unable to delete not instanced Song")
        else:
            self.__songs.remove(song)
