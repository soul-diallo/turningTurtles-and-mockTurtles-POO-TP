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
            if self.r.getListCoin()[num_case - 1].getFace() == 0:
                sortie = False
        return num_case

    def firstMove(self):
        # Appel de la classe chooseHead qui va choisir une piece Face
        case = self.chooseHead() - 1
        # On recupere la piece correspondante a la position de case
        p = self.r.getCoin(case)
        p.turnCoin()
        self.r.affichage()
        return case

    def chooseCoin(self, indice):
        """
        Fonction qui prend en indice une case de la rangee autre que la premiere
        Elle demande au joueur courant de saisir un numéro d'une case strictement inférieur a celui passé en parametre.
        Tant que le numero saisi ne sera pas valide, on le fera saisir de nouveau. Finalement, la methode retournera
        ce numero.
        :param indice:
        :return: ind_case
        """
        ind_case = 1
        sortie = True
        while sortie:
            ind_case = int(input("Choisir une case a gauche"))
            if self.r.getListCoin()[ind_case -1].getFace() < indice:
                sortie = False
        return ind_case

    def secondMove(self, indice):
        """
        Cette methode prenant en parametre l'indice d'une case de la rangee autre que la premiere. Elle appelle la
        methode chooseCoin et met a jour la rangee de pieces.
        :param indice:
        :return:
        """


    def anotherMove(self):
        pass

    def gameplay(self):
        pass


c = turningTurtles(9)

c.firstMove()
