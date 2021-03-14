class Coin:
    def __init__(self, face=True):
        self.__face = face

    def setFace(self,face):
        self.__face = face

    def getFace(self):
        return self.__face

