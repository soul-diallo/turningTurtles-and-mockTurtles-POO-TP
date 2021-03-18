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

    # Fonction retournant True si toutes les pièces de la rangée sont sur leur coté pile ou False sinon
    def allPile(self):
        for k in range (self.__nbrPieceRangee):
            if self.__listCoin[1].getFace() == 1:
                etat = True
            else:
                etat = False
            return etat


c = Row(9)
print(c.affichage())
print(c.allPile())