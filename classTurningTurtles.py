import classPlayer
import classRow


class turningTurtles:
    # Attributs de la classe
    joueurs = []

    r = classRow.Row()

    # Constructeur de la classe
    def __init__(self, nbrPiece):
        self.__nbrPiece = nbrPiece
        for i in range(1, 3):
            print("Nom du Joueur", i)
            name = input()
            self.joueurs.append(classPlayer.Player(name))

    def afficher(self):
        print(self.joueurs[0].getName())


c = turningTurtles(9)
c.afficher()
