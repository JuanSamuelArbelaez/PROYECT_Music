import string
from Model.Assets.Admin.Admin import Admin
from Model.Assets.Artist import Artist
from Model.Assets.Song import Song
from Model.Assets.User import User
from Model.Structures.BinaryTree.BinaryTree import BinaryTree
from Model.Structures.HashMap.HashMap import HashMap
from Model.Structures.LinkedList.LinkedList import LinkedList


class MusicApp:
    def __init__(self):
        self.__artist = BinaryTree[Artist]()
        self.__songs = LinkedList[Song]()
        self.__users = HashMap[User]()
        self.__admin = Admin("Robin", "0todos", "robin@musicapp.com")

    def add_song(self, song: Song):
        if song is None:
            raise AttributeError("Song can't be None")
        if song.get_artist() is None:
            raise AttributeError("Artist can't be None")
        if not self.__artist.contains(song.get_artist()):
            raise AttributeError("Artist not found")
        else:
            song.get_artist().add_song(song)
            self.__songs.append(song)

    def add_artist(self, artist: Artist):
        self.__artist.add(artist)
        self.__artist.balance()

    def add_user(self, user: User):
        self.__users.put_in(user.get_username(), user)

    def add_song_tag(self, song: Song, tag: string):
        if song.contains_true_tag(tag):
            raise AttributeError("Tag already assigned here")
        else:
            song.add_tag(tag)

    def remove_song_tag(self, song: Song, tag: string):
        if not song.contains_true_tag(tag):
            raise AttributeError("Unable to delete tab not assigned")
        else:
            song.remove_tag(tag)

    def remove_song(self, song: Song):
        if not self.__songs.contains(song):
            raise AttributeError("Unable to delete not instanced Song")
        else:
            self.__songs.remove(song)

    def get_songs(self):
        return self.__songs

    def add_user_song(self, user: User, song: Song):
        if not self.__songs.contains(song):
            raise AttributeError("Song not founded")
        if not self.__users.contains_value(user):
            raise AttributeError("User not founded")
        user.add_song(song)

    def remove_user_song(self, user: User, song: Song):
        if not self.__songs.contains(song):
            raise AttributeError("Song not founded")
        if not self.__users.contains_value(user):
            raise AttributeError("User not founded")
        user.delete_song(song)
