from Model.Structures.CircularList.CircularList import CircularList


class User:
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__song_list = CircularList()

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_song_list(self):
        return self.__song_list

    def set_song_list(self, song_list):
        self.__song_list = song_list

    def add_song(self, song):
        self.__song_list.append(song)

    def delete_song(self, song):
        self.__song_list.remove_value(song)

    def sort_song_list(self, key):
        self.__song_list.sort(key)
