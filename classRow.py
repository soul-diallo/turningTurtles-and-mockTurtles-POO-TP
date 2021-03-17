from random import randint
import classCoin


class Row:
    def __init__(self, nbrPieceRangee, listCoin=[]):
        self.__nbrPieceRangee = nbrPieceRangee
        self.__listCoin = listCoin

        for i in range(self.__nbrPieceRangee):
            alea = randint(0, 1)
            listCoin.append(classCoin.Coin(alea))

    def affichage(self):
        for i in range(self.__nbrPieceRangee ):
            if self.__listCoin[i].getFace() == 0:
                print("H", end=" ")
            else:
                print("T", end=" ")
        print("")
        for i in range(1,self.__nbrPieceRangee + 1):
            print(i, end=" ")



a = Row(9)
a.affichage()
