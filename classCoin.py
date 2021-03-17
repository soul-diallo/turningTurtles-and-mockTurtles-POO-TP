from random import randint


class Coin:
    """ Implementation de la classe Coin avec un attribut de type booléen
     True correspond à Face
      False correspond à Pile
      """

    def __init__(self, face=True):
        self.__face = face

    def setFace(self, face):
        self.__face = face

    def getFace(self):
        return bool(self.__face)

    def turnCoin(self):
        self.__face = False
