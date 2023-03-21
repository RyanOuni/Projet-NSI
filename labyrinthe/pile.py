"""
Implémentation d'une pile respectant l'interface fonctionnelle de l'annale
du sujet zéro du baccalauréat 2021
"""

def creer_pile_vide():
    """
    Renvoie une pile vide, représentée, par une liste
    """
    return []


def est_vide(P):
    """
    Renvoie True si la pile P est vide, et False sinon
    Paramètres :
    ------------
        P : une pile représentée par une liste Python
    Sortie :
    --------
        bool : True si P est vide, et False sinon
    """
    return P == []


def empiler(P, x):
    """
    empile l'élément x au sommet de la pile P
    Paramètres :
    ------------
        P : une pile représentée par une liste Python
        x : un élément de type quelconque
    Sortie :
    --------
        None
    """
    P.append(x)


def depiler(P):
    """
    Dépile la pile P, supposée non vide,
    et renvoie l'élément au sommet de la Pile P
    Paramètres :
    ------------
        P : une pile représentée par une liste Python
    Sortie :
    --------
        l'élément au sommet de P. Si P est vide renvoie un message d'erreur.
    """
    return P.pop()


def afficher_pile(P):
    """
    Affiche la Pile P, sans en modifier le contenu
    """
    for i in range(-1, -len(P)-1, -1):
        print(f"|  {P[i]}")
    print("----------")