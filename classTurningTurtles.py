import classPlayer
import classRow


class turningTurtles:
    # Constructeur de la classe
    def __init__(self, nbrPiece):
        # Liste de deux objets joueurs
        self.joueurs = []
        # Un objet de la classe Row
        self.r = classRow.Row(nbrPiece)
        # Nombre de pieces de la rangee
        self.__nbrPiece = nbrPiece
        for i in range(1, 3):
            print("Nom du Joueur", i)
            name = input()
            self.joueurs.append(classPlayer.Player(name))

    def afficher(self):
        print(self.joueurs[0].getName())

    def chooseHead(self):
        num_case = 0
        sortie = True
        while sortie:
            num_case = int(input("Choisir une case qui a une piece cote face"))
            if self.r.getListCoin()[num_case].getFace() == 0:
                sortie = False
        return num_case

    def firstMove(self):
        # Appel de la classe chooseHead qui va choisir une piece Face
        case = self.chooseHead()




# c = turningTurtles(9)
# c.afficher()
# print(c.chooseHead())
