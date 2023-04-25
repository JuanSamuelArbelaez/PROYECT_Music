from Model.Structures.CircularList.CircularList import CircularList


class User:
    def __init__(self, username, password, email, songList=None):
        self._username = username
        self._password = password
        self._email = email
        self._song_list = CircularList()

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_song_list(self):
        return self._song_list

    def set_song_list(self, song_list):
        self._song_list = song_list

    def add_song(self, song):
        self._song_list.append(song)

    def delete_song(self, song):
        self._song_list.remove_value(song)

