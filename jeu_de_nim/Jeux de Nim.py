def init_plateau(n):
    """la fonction init_plateau(n) retourne un tableau de n fois le
    même caractère '|'.
    exemple:
    >>> init_plateau(5)
    ['|', '|', '|', '|', '|']
    """
    plateau = ["|"] * n
    return plateau


def coup_possible(nb_alumette, plateau, k):
    """ la fonction coup_possible(nb_alumette, plateau,k) retourne si
    un coup est possible.
    Si le nombre d'alumettes choisis par le joueur est:
     - inférieur au égal à k, et
     - inférieur ou égal au nombre d'alumettes disponibles, c'est à dire à la
     longueur de la liste plateau, et
     - supérieur ou égal à 0
     alors la fonction retourne True
     sinon la fonction retourne False

    exemple:
    >>> coup_possible(4, ['|', '|', '|', '|', '|'],3)
    False
    >>> coup_possible(3, ['|', '|', '|', '|', '|'],3)
    True
    >>> coup_possible(3, ['|', '|'],3)
    False
    """
    if nb_alumette <= len(plateau) and nb_alumette <= k and nb_alumette > 0:
        return True
    else:
        return False


def jouer_coup(nb_alumette, plateau):
    """la fonction jouer_coup(nb_alumette, plateau) enlève de
    la liste plateau (sur place) le nombre d'alumettes nb_alumette.

    exemple:
    >>> plateau = ['|', '|', '|', '|', '|']
    >>> jouer_coup(3, plateau)
    >>> plateau
    ['|', '|']
    """
    for i in range(nb_alumette):
        plateau.pop()


def victoire(plateau):
    """la fonction victoire(plateau) vérifie qu'il reste reste des
    alumettes sur le plateau.
    Si la longueur de la liste plateau est nulle, la fonction
    retourne True.
    Sinon la fonction retourne False.

    exemple:
    >>> victoire(['|', '|'])
    False
    >>> victoire([])
    True
    """
    if len(plateau) == 0:
        return True
    return False


def entree_joueurs():
    """
    la fonction entree_joueurs() demande le nom des deux joueurs
    et les retournent dans une liste

    exemple:
    >>> joueurs = entree_joueurs()
    >>> joueurs
    ['Bob', 'Alice']
    """
    joueurs = []
    for i in range(2):
        joueur = input("Entrez le nom du joueur " + str(i + 1) + " ")
        joueurs.append(joueur)
    return joueurs


def affiche_plateau(plateau):
    """la fonction affiche_plateau(plateau) affiche une chaine de
    caractère composé des éléments de la liste plateau séparés
    d'un espace.

    exemple:
    >>> affiche_plateau(['|', '|', '|', '|', '|'])
    | | | | |
    """
    print(" ".join(plateau))


def entree_coup(joueurs, joueur_actif, plateau, k):
    """la fonction entree_coup(joueurs, joueur_actif, plateau, k) demande au joueur
    actif combien il veut enlever d'alumettes. La saisie est contôlée en
    vérifiant que le coup est possible (vous pouvez utiliser la fonction coup_possible
    définie précédemment).

    exemple:
    >>> coup = entree_coup(['Bob', 'Alice'], 1, ['|', '|', '|', '|'], 3)
    Alice combien voulez vous en enlever ? 5
    Impossible.
    Alice combien voulez vous en enlever ? 3
    >>> coup
    """
    coup = int(input(joueurs[joueur_actif]
                     + " combien voulez vous en enlever ? "))
    while not coup_possible(coup, plateau, 3):
        coup = int(input(joueurs[joueur_actif]
                         + " combien voulez vous en enlever ? "))
    return coup


def tour(joueurs, joueur_actif, plateau, k):
    """la fonction tour(joueurs, joueur_actif, plateau, k) réalise un tour complet
    du jeu de nim:
     1. Demande à entrer un coup au joueur actif joueur_actif.
     2. Joue le coup choisi par le joueur actif.
     3. Affiche le plateau.
     4. Test si il y a une fin de jeu (victoire).
    Cette fonction retourne True si il y a une fin de jeu (victoire), False sinon.

    Considérez que toutes les fonctions précédemment demandées sont faites et
    fonctionnent correctement

    exemple:
    >>> plateau = ['|', '|', '|', '|']
    >>> fin = tour(['Bob', 'Alice'], 1, plateau, 3)
    Alice combien voulez vous en enlever ? 5
    Impossible.
    Alice combien voulez vous en enlever ? 3
    >>> fin
    False
    >>> plateau
    ['|']
    >>> fin = tour(['Bob', 'Alice'], 0, plateau, 3)
    Bob combien voulez vous en enlever ? 1
    >>> fin
    True
    >>> plateau
    []
    """
    coup = entree_coup(joueurs, joueur_actif, plateau, k)
    jouer_coup(coup, plateau)
    affiche_plateau(plateau)
    fin = victoire(plateau)
    return fin


def jeu_de_nim(n, k):
    """la fonction jeu_de_nim(n, k) implémente le jeu de nim pour n alumettes
    initiales dans lequel on ne peut jamais tirer plus de k alumettes
    à chaque tour. Cette fonction réalise les étapes suivantes:
     1. Demande le nom des joueurs,
     2. Initialise le plateau,
     3. Affiche le plateau,
     4. Réalise les tours de jeu jusqu'à la fin de la partie
     5. Affiche "nom du gagnant vous avez gagné !"
    Cette fonction retourne le nom du gagnant.

    Considérez que toutes les fonctions précédemment demandées sont faites et
    fonctionnent correctement.

    exemple:
    >>> gagnant = jeu_de_nim(21, 3)
    Entrez le nom du joueur 1 Bob
    Entrez le nom du joueur 2 Alice
    | | | | | | | | | | | | | | | | | | | | |
    Bob combien voulez vous en enlever ? 3
    | | | | | | | | | | | | | | | | | |
    Alice combien voulez vous en enlever ? 4
    Impossible.
    Alice combien voulez vous en enlever ? 3
    | | | | | | | | | | | | | | |
    Bob combien voulez vous en enlever ? 3
    | | | | | | | | | | | |
    Alice combien voulez vous en enlever ? 3
    | | | | | | | | |
    Bob combien voulez vous en enlever ? 3
    | | | | | |
    Alice combien voulez vous en enlever ? 3
    | | |
    Bob combien voulez vous en enlever ? 2
    |
    Alice combien voulez vous en enlever ? 0
    Impossible.
    Alice combien voulez vous en enlever ? 1

    Bob vous avez gagné !
    >>> gagnant
    'Bob'
    """
    fin = False
    joueurs = entree_joueurs()
    plateau = init_plateau(n)
    affiche_plateau(plateau)
    joueur_actif = 0
    while not fin:
        fin = tour(joueurs, joueur_actif, plateau, k)
        joueur_actif = 1 - joueur_actif
    print(joueurs[joueur_actif], "vous avez gagné !")
    return joueurs[joueur_actif]


gagnant = jeu_de_nim(21, 3)
