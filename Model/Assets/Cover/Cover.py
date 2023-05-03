from Model.Tools.FileManager.FileManager import retrieve_image

class Cover:
    def __init__(self, code: str, url, path: str):
        self.__id = code
        self.__url = url
        self.__img = retrieve_image(code, url, path)
