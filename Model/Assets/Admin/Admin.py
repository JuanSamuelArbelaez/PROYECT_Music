class Admin:
    def __init__(self, username: str, password: str, email: str):
        self.__username = username
        self.__password = password
        self.__email = email

    def get_username(self) -> str:
        return self.__username

    def set_username(self, username: str):
        self.__username = username

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str):
        self.__password = password

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

