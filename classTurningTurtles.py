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
            if self.r.getListCoin()[ind_case - 1].getFace() < indice:
                sortie = False
        return ind_case

    def secondMove(self, indice):
        """
        Cette methode prenant en parametre l'indice d'une case de la rangee autre que la premiere. Elle appelle la
        methode chooseCoin et met a jour la rangee de pieces.
        :param indice:
        :return:
        """
        indice_case = self.chooseCoin(indice)
        p = self.r.getCoin(indice_case)
        p.turnCoin()
        self.r.affichage()

    def anotherMove(self, indice):
        """
        Cette methode prend en parametre l'indice d'une case de la rangee. Si cette case n'est pas la premiere, elle
        demande au joueur courant de saisir un entier egal à 0 ou a 1 afin d'indiquer s'il souhaite effectuer son coup
        facultatif ou non. Tant que la saisie ne sera pas valide, elle sera recommencee. En fonction de la saisie, elle
        appelle ou non la methode secondMove.
        :param indice:
        :return:
        """
        choix = 0
        if self.r.getListCoin()[indice].getFace() != 0:
            sortie = True
            while sortie:
                choix = int(input("Faites vous un coup facultatif ? 0 pour NON et 1 pour OUI"))
                if choix != 0 and 1:
                    sortie = False

        if choix == 1:
            self.secondMove(indice)

    def gameplay(self):
        fin_game = False
        #b = self.r.allPile()
        while not fin_game:
            self.firstMove()
            b = self.r.allPile()

            if b:
                fin_game = True
                print(fin_game)


c = turningTurtles(9)

c.gameplay()
