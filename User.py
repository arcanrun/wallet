from b import *


class User:

    def __init__(self, name, zarp, day):
        self.__wallet = Budget(name, zarp, day)

    def get_user(self):
        return self.__wallet