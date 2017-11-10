class User:
    def __init__(self):
        self.__id = ''
        self.__password = ''
        self.__type = ''
    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_type(self):
        return self.__type

    def set_id(self, id):
        self.__id = id
    def set_password(self, password):
        self.__password = password
    def set_type(self, type):
        self.__type = type
