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
        for i in range(self.__nbrPieceRangee):
            if self.__listCoin[i].getFace() == 0:
                print("H", end=" ")
            else:
                print("T", end=" ")
        print("")
        for j in range(1, self.__nbrPieceRangee + 1):
            print(j, end=" ")
        print("")

    # Fonction retournant True si toutes les pièces de la rangée sont sur leur coté pile ou False sinon
    def allPile(self):
        # Fonction all qui prend un iterable en tant qu'entree et renvoie <<True>> si tous les elements de cette
        # derniere sont <<True>>. Sinon <<False>>.
        if all(x == self.__listCoin[0] for x in self.__listCoin):
            return True
        else:
            return False


