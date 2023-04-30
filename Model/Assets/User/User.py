import string

from Model.Assets.Song import Song
from Model.Structures.CircularList.CircularList import CircularList
from Model.Tools.UndoRedoManager.UndoRedoManager import UndoRedoManager


class User:
    def __init__(self, username: str, password: str, email: str):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__song_list = CircularList()
        self.__undo_redo_manager = UndoRedoManager()

    def get_username(self):
        return self.__username

    def set_username(self, username: str):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password: str):
        self.__password = password

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_song_list(self):
        return self.__song_list

    def set_song_list(self, song_list: CircularList[Song]):
        self.__song_list = song_list

    def add_song(self, song: Song):
        if self.__song_list.contains(song):
            raise AttributeError("This song is already here")
        else:
            def add_song_operation():
                self.__song_list.append(song)
            self.__undo_redo_manager.do_operation(add_song_operation)

    def delete_song(self, song: Song):
        if not self.__song_list.contains(song):
            raise AttributeError("Can't remove song that's not already here")
        else:
            def remove_song_operation():
                self.__song_list.remove_value(song)

            self.__undo_redo_manager.do_operation(remove_song_operation)

    def sort_song_list(self, key):
        self.__song_list.sort(key)

    def undo(self):
        self.__undo_redo_manager.undo()

    def redo(self):
        self.__undo_redo_manager.redo()

    def contains_song(self, song: Song):
        return self.__song_list.contains(song)