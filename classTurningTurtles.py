import classPlayer
import classRow


class turningTurtles:
    # Constructeur de la classe
    def __init__(self, nbrPiece):
        # Liste de deux objets joueurs
        self.joueurs = []
        # Nombre de pieces de la rangee
        self.__nbrPiece = nbrPiece
        for i in range(1, 3):
            print("Nom du Joueur", i)
            name = input()
            self.joueurs.append(classPlayer.Player(name))

        # Un objet de la classe Row et son affichage
        self.r = classRow.Row(nbrPiece)
        self.r.affichage()

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
        # On recupere la piece correspondante a la position de case
        p = self.r.getCoin(case)
        p.turnCoin()
        self.r.affichage()


c = turningTurtles(9)

c.firstMove()
