from davistk import *
from time import sleep
from random import randint

# dimensions du jeu
hauteur_pong = 100
largeur_pong = 10
largeur_fenetre = 640
hauteur_fenetre = 480
distance_pong_bord = 30
rayon_balle = 10

# themes
couleur_fond = "black"
couleur_pong = "white"
couleur_balle = "white"

# vitesses
vitesse_balle = 8


# Ne pas modifier :
def affiche_balle(position_balle):
    """ Ne pas modifier. Affiche un cercle correspondant à la balle à la
    position position_balle où position_balle est un couple (tuple) de
    coordonnées.
    Parameters:
        position_balle (int,int): couple des coordonnées de la balle
    """
    x, y = position_balle
    cercle(x, y, rayon_balle, couleur_balle, couleur_balle)

# Ne pas modifier :
def affiche_pong(position_pong, droite_gauche):
    """ Ne pas modifier. Affiche un rectangle correspondant à la raquette
    centré à la position position_pong où position_pong est l'ordonnée de la
    position de la raquette.
    Peut afficher la raquette à gauche ou à droite en fonction du
    paramètre droite_gauche
    Parameters:
        position_pong (int): ordonnée de la raquette
        droite_gauche (str): prend les valeurs "gauche" ou "droite" en
        fonction de la raquette à afficher
    """
    if droite_gauche == "gauche":
        x = distance_pong_bord
    else:
        x = largeur_fenetre - distance_pong_bord
    y = position_pong
    rectangle(x-largeur_pong/2, y-hauteur_pong/2,
              x+largeur_pong/2, y+hauteur_pong/2, couleur_pong, couleur_pong)

# Ne pas modifier :
def mouvement_ordi(position_balle, position_pong1):
    """ Ne pas modifier, gère le déplacement de l'ordinateur """
    x, y = position_balle
    if y > position_pong1 + hauteur_pong / 4:
        return position_pong1 + 5
    elif y < position_pong1 - hauteur_pong / 4:
        return position_pong1 - 5
    else:
        return position_pong1

# Ne pas modifier :
def detection_impact_pong(
        position_pong1, position_pong2, position_balle, direction_balle):
    """ Ne pas modifier. Fonction permettant de détecter l'impact entre une
    raquette et la balle et changeant la direction de celle-ci """
    x, y = position_balle
    dx, dy = direction_balle
    x_pong1, y_pong1 = distance_pong_bord, position_pong1
    x_pong2, y_pong2 = largeur_fenetre - distance_pong_bord, position_pong2
    balle_sur_pong1 = y < y_pong1 + hauteur_pong / 2 and \
        y > y_pong1 - hauteur_pong / 2 and \
        x - rayon_balle < x_pong1 + largeur_pong / 2 and \
        x - rayon_balle > x_pong1 - largeur_pong / 2
    balle_sur_pong2 = y < y_pong2 + hauteur_pong / 2 and \
        y > y_pong2 - hauteur_pong / 2 and \
        x + rayon_balle < x_pong2 + largeur_pong / 2 and \
        x + rayon_balle > x_pong2 - largeur_pong / 2
    if balle_sur_pong1:
        return -dx, dy + (y - y_pong1)/100
    if balle_sur_pong2:
        return -dx, dy + (y - y_pong2)/100
    return dx, dy

# Ne pas modifier :
def deplacement_balle(position_balle, direction_balle):
    ''' Ne pas modifier. Permet de calculer la nouvelle position de la balle à partir de
    sa position initiale et de la direction (mouvement) dans laquelle elle va.
    Parameters:
        position_balle (float, float): couple de coordonnées de la balle
        direction_balle (float, float): couple de déplacement à ajouter aux
        coordonnées
    Returns:
        (float, float): nouvelles coordonnées de la balle
    '''
    x, y = position_balle
    dx, dy = direction_balle
    return x + dx, y + dy

# A modifier : - Modifié et fini !
def change_direction_pong2(touche):
    """ Retourne le déplacement de la raquette en ordonnée (en pixel).
    Si la touche appuyée est "Up" alors retourne -5
    Si la touche appuyée est "Down" alors retourne 5
    Sinon retourne 0
    Parameters:
        touche (str): nom de la touche pressée
    Returns:
        (int): déplacement en ordonnée de la raquette
    """
    if touche == "Up" : # renvoie -5 si la touche == "Up"
        return -5
    elif touche == "Down" : # renvoie 5 si la touche == "Down"
        return 5
    else : # renvoie 0 si ni Up ni Down est rentré
        return 0 

# A modifier : - Modifié et fini !
def detection_bord(position_balle, direction_balle):
    """ Permet de détecter l'impact de la balle sur le bord supérieur
    ou inférieur de la fenêtre. Renvoie la nouvelle direction de la balle
    Parameters:
        position_balle (float, float): couple des coordonnées de la balle
        direction_balle(float, float): couple correspondant à la vitesse
        horizontale et verticale de la balle
    Returns:
        (float, float): couple correspondant à la vitesse horizontale
        et verticale de la balle après impact éventuel avec le bord.
    """
    x, y = position_balle  # récupère l'abscisse et l'ordonnée de la balle
    dx, dy = direction_balle  # récupère la direction de la balle suivant les abscisses et suivant les ordonnées
    if y < 0 + rayon_balle or y > hauteur_fenetre - rayon_balle: # sert a renvoyer la balle si elle touche le haut ou le bas
        return dx, -dy # si la balle touche le haut ou le bas, on renvoie la direction opposée en vertical
    else : 
        return dx, dy # si aucun bord n'est touché, on renvoie les directions sans les changer

# A modifier : - Modifié et fini !
def detection_sortie(position_balle):
    ''' Permet de détecter la sortie de la balle d'un côté ou d'un autre.
    Renvoie la chaine de caractère "pong1" si la balle sort à gauche, "pong2"
    elle sort à droite, "continue" sinon.
    Parameters:
        position_balle (float, float): couple des coordonnées de la
        balle_sur_pong1
    Returns:
        (string): "pong1" si la balle sort à gauche, "pong2"
        elle sort à droite, "continue" sinon
    '''
    x, y = position_balle  # récupère l'abscisse et l'ordonnée de la balle
    if x <= 0 : # renvoie pong1 si la balle touche le côté gauche
        return "pong1"
    elif x >= largeur_fenetre : # renvoie pong2 si la balle touche le côté droit
        return "pong2"
    else :  # renvoie continue si la balle ne touche aucun des deux côtés
        return "continue"

# A modifier : - Modifié et fini !
def deplacement_pong(position_pong, direction_pong):
    ''' Permet de calculer la nouvelle position d'une raquette à partir de
    sa position initiale et de la direction (mouvement) dans laquelle elle va.
    Parameters:
        position_pong (int): ordonnée de la raquette
        direction_pong (int): déplacement à ajouter à l'ordonnée
    Returns:
        (int): nouvelle ordonnée de la raquette
    '''
    position_pong = position_pong + direction_pong
    return position_pong

# A modifier : - Modifié et fini !
def fin_de_jeu(sortie):
    ''' Permet de sortir de la boucle principale du jeu.
    Parameters:
        sortie (str): information de sortie d'un côté ("pong1), de l'autre
        ("pong2") ou de non sortie ("continue")
    Returns:
        (bool): True si la balle est sortie, False sinon
    '''
    if sortie == "pong1" or sortie == "pong2":
        return True
    elif sortie == "continue":
        return False

# A modifier :
def affiche_victoire(sortie):
    ''' Fonction permettant de gérer graphiquement la fin de jeu
    Parameters:
        sortie (str): information de sortie d'un côté ("pong1), de l'autre
        ("pong2") ou de non sortie ("continue")
    Returns:
        ...
    '''
    if sortie == "pong1": # choses à afficher si la balle est sortie du coté gauche (J1 Win)
        texte(largeur_fenetre/2, hauteur_fenetre/2, "IA Lose - Win J1", couleur=couleur_pong, taille=30, ancrage="center")
        texte(largeur_fenetre/2, hauteur_fenetre/1.7, "Vous avez gagné !", couleur=couleur_pong, taille=16, ancrage="center")
        texte(largeur_fenetre/2, hauteur_fenetre/1.5, "Votre score est de :", couleur=couleur_pong, taille=12, ancrage="center")
        texte(largeur_fenetre/2, hauteur_fenetre/1.4, int(temps), couleur=couleur_pong, taille=18, ancrage="center")
    elif sortie == "pong2": # choses à afficher si la balle est sortie du coté droit (J2 Win)
        texte(largeur_fenetre/2, hauteur_fenetre/2, "IA Win - Lose J1", couleur=couleur_pong, taille=30, ancrage="center")
        texte(largeur_fenetre/2, hauteur_fenetre/1.7, "Vous avez perdu !", couleur=couleur_pong, taille=16, ancrage="center")
        texte(largeur_fenetre/2, hauteur_fenetre/1.5, "Votre score est de :", couleur=couleur_pong, taille=12, ancrage="center")
        texte(largeur_fenetre/2, hauteur_fenetre/1.4, int(temps), couleur=couleur_pong, taille=18, ancrage="center")
    elif sortie == "continue":
        return None
    attend_ev()


# programme principal
if __name__ == "__main__":
    # initialisation du jeu
    framerate = 20    # taux de rafraîchissement du jeu en images/s
    # la vitesse de la balle est située plus bas pour que le choix de difficulté fonctionne
    position_balle = (320, 240)  # position initiale de la balle
    position_pong1 = 240
    position_pong2 = 240
    cree_fenetre(largeur_fenetre, hauteur_fenetre)

    # menus
    jouer = True
    menu = True
    instructions = True
    theme = True
    difficulty = True
    
    entree = False # mettre ce paramètre en True ajoutera un ecran de départ supplementaire, jugé inutile en cours de route
    ttext=0
    loading = 0

    while entree :
        for i in range(8):
            efface_tout
            rectangle(0, 0, largeur_fenetre, hauteur_fenetre, couleur='darkcyan', remplissage='darkcyan')
            texte(largeur_fenetre/2, hauteur_fenetre/2, "Davis Games", "white", ancrage="center", taille=ttext, police="Century Gothic")
            loading = loading + 75
            ligne(0, hauteur_fenetre/1.3, largeur_fenetre, hauteur_fenetre/1.3, couleur='black', epaisseur=24)
            ligne(0, hauteur_fenetre/1.3, 50+loading, hauteur_fenetre/1.3, couleur='grey', epaisseur=20)
            texte(largeur_fenetre/6, hauteur_fenetre/1.3, "Loading ...", "white", ancrage="center", taille=12, police="Century Gothic")
            ttext = ttext + 2
            efface_tout
            attente(0.3)
        break


    while menu :
        # affichage des éléments
        rectangle(0, 0, largeur_fenetre, hauteur_fenetre, couleur='darkcyan', remplissage='darkcyan')
        texte(largeur_fenetre/2, hauteur_fenetre/8, "PONG !", "white", ancrage="center", taille=42, police="Rockwell")
        texte(largeur_fenetre/1.6, hauteur_fenetre/5.7, "EXTREME", "red", ancrage="center", taille=20, police="Rockwell")
        cercle(440, 50, 20, couleur='white', remplissage='white', epaisseur=2)
        texte(largeur_fenetre/1.5, hauteur_fenetre - 15, "Un jeu conçu par Andrei et Noa", "white", taille=10, ancrage="w", police="Century Gothic")
        texte(largeur_fenetre/2, hauteur_fenetre - 15, "(c) Davis Games 2023", "white", taille=10, ancrage="center", police="Century Gothic")
        texte(largeur_fenetre-610, hauteur_fenetre - 15, "v.2023", "white", taille=10, ancrage="c", police="Century Gothic")
        # bouton jouer
        rectangle(largeur_fenetre-450, hauteur_fenetre-200, largeur_fenetre-190, hauteur_fenetre-250, couleur='black', remplissage='black', epaisseur=6)
        rectangle(largeur_fenetre-450, hauteur_fenetre-200, largeur_fenetre-190, hauteur_fenetre-250, couleur='white', remplissage='white')
        texte(largeur_fenetre/2, hauteur_fenetre-225, "NORMAL GAME", couleur="black", taille = 20, police = "Courier", ancrage="center")
        # bouton jouer custom
        rectangle(largeur_fenetre-450, hauteur_fenetre-190, largeur_fenetre-190, hauteur_fenetre-140, couleur='black', remplissage='black', epaisseur=6)
        rectangle(largeur_fenetre-450, hauteur_fenetre-190, largeur_fenetre-190, hauteur_fenetre-140, couleur='white', remplissage='white')
        texte(largeur_fenetre/2, hauteur_fenetre-165, "CUSTOM GAME", couleur="black", taille = 20, police = "Courier", ancrage="center")
        # bouton exit game
        rectangle(largeur_fenetre-450, hauteur_fenetre-130, largeur_fenetre-190, hauteur_fenetre-80, couleur='black', remplissage='black', epaisseur=6)
        rectangle(largeur_fenetre-450, hauteur_fenetre-130, largeur_fenetre-190, hauteur_fenetre-80, couleur='white', remplissage='white')
        texte(largeur_fenetre/2, hauteur_fenetre-105, "EXIT GAME", couleur="black", taille = 20, police = "Courier", ancrage="center")

        while True:
            ev = donne_ev()
            tev = type_ev(ev)

            if tev == "ClicGauche": # si l'utilisateur clique entre ax et ay et bx et by faire ceci ou cela...
                if abscisse(ev) > largeur_fenetre-450 and abscisse(ev) < largeur_fenetre-190 and ordonnee(ev) > hauteur_fenetre-250 and ordonnee(ev) < hauteur_fenetre-200 :
                    theme = False
                    difficulty = False
                    break
                if abscisse(ev) > largeur_fenetre-450 and abscisse(ev) < largeur_fenetre-190 and ordonnee(ev) > hauteur_fenetre-190 and ordonnee(ev) < hauteur_fenetre-140 :
                    break
                if abscisse(ev) > largeur_fenetre-450 and abscisse(ev) < largeur_fenetre-190 and ordonnee(ev) > hauteur_fenetre-130 and ordonnee(ev) < hauteur_fenetre-80 :   
                    instructions = False
                    theme = False
                    difficulty = False
                    jouer = False
                    break
            elif tev == 'Quitte':  # on sort de la boucle
                instructions = False
                theme = False
                difficulty = False
                jouer = False # si l'utilisateur quitte, on ne lance pas le jeu
                break
            else:  # dans les autres cas, on ne fait rien
                pass
            mise_a_jour()
        break

    while instructions :
        # affichage des éléments
        rectangle(0, 0, largeur_fenetre, hauteur_fenetre, couleur='brown', remplissage='indianred')
        # deco carré Up
        rectangle(largeur_fenetre-600, hauteur_fenetre-350, largeur_fenetre-550, hauteur_fenetre-300, couleur='black', remplissage='black', epaisseur=4)
        rectangle(largeur_fenetre-600, hauteur_fenetre-350, largeur_fenetre-550, hauteur_fenetre-300, couleur='white', remplissage='white', epaisseur=1)
        ligne(largeur_fenetre-575, hauteur_fenetre-310, largeur_fenetre-575, hauteur_fenetre-338, couleur='black', epaisseur=6) 
        fleche(largeur_fenetre-575, hauteur_fenetre-310, largeur_fenetre-575, hauteur_fenetre-338, couleur='black', epaisseur=10)
        # deco carré Down
        rectangle(largeur_fenetre-600, hauteur_fenetre-275, largeur_fenetre-550, hauteur_fenetre-225, couleur='black', remplissage='black', epaisseur=4)
        rectangle(largeur_fenetre-600, hauteur_fenetre-275, largeur_fenetre-550, hauteur_fenetre-225, couleur='white', remplissage='white', epaisseur=1)
        ligne(largeur_fenetre-575, hauteur_fenetre-263, largeur_fenetre-575, hauteur_fenetre-235, couleur='black', epaisseur=6) 
        fleche(largeur_fenetre-575, hauteur_fenetre-263, largeur_fenetre-575, hauteur_fenetre-235, couleur='black', epaisseur=10)
        # texte
        texte(largeur_fenetre/2, hauteur_fenetre/15, "Instructions", couleur="white", ancrage = "n", police = "Courier")
        texte(largeur_fenetre-500, hauteur_fenetre/5, "Touches : ", couleur="white", taille = 12, ancrage = "e", police = "Courier")
        texte(largeur_fenetre-540, hauteur_fenetre-330, "Fait bouger votre Raquette vers le haut de l'écran", couleur="white", taille = 12, police = "Courier")
        texte(largeur_fenetre-540, hauteur_fenetre-260, "Fait bouger votre Raquette vers le bas de l'écran", couleur="white", taille = 12, police = "Courier")
        texte(largeur_fenetre-480, hauteur_fenetre/1.7, "Consignes : ", couleur="white", taille = 12, ancrage = "e", police = "Courier")
        texte(largeur_fenetre-10, hauteur_fenetre/1.5, """
        L'objectif est simple : envoyer la balle dans le camp adverse et c'est gagné.
        Bien evidemment l'intelligence artificielle tentera de vous en empecher.
        Ne laissez pas la balle arriver dans votre camp sinon c'est perdu.
        Vous avez tout compris ? Alors bonne chance ! """, couleur="white", taille = 10, ancrage = "e", police = "Courier")
        texte(largeur_fenetre-120, hauteur_fenetre/1.2, "Appuyez sur une touche pour continuer", couleur="white", taille = 14, ancrage = "e", police = "Courier")
        while True:
            ev = donne_ev()
            tev = type_ev(ev)

            if tev == 'Touche': # appuyer sur une touche fait sortir de la boucle pour passer au prochain menu
                break
            elif tev == 'Quitte':  # on sort de la boucle
                theme = False
                difficulty = False
                jouer = False # si l'utilisateur quitte, on ne lance pas le jeu
                break
            else:  # dans les autres cas, on ne fait rien
                pass
            mise_a_jour()
        break

    while difficulty :
        # affichage des éléments
        rectangle(0, 0, largeur_fenetre, hauteur_fenetre, couleur='brown', remplissage='brown')
        texte(largeur_fenetre/2, hauteur_fenetre/15, "Choissisez un niveau de difficulté", couleur="white", taille = 16, ancrage = "n", police = "Courier")
        texte(largeur_fenetre - 600, hauteur_fenetre/5, "Appuyez sur ou cliquez : ", couleur="white", taille = 12, police = "Courier")
        texte(largeur_fenetre - 600, hauteur_fenetre-100, "Note : Le niveau de difficulté influence la vitesse de la balle.", couleur="white", taille = 10, police = "Courier")
        # carré easy
        rectangle(largeur_fenetre-595, hauteur_fenetre-300, largeur_fenetre-445, hauteur_fenetre-200, couleur='black', remplissage='black', epaisseur=6)
        rectangle(largeur_fenetre-595, hauteur_fenetre-300, largeur_fenetre-445, hauteur_fenetre-200, couleur='white', remplissage='white')
        # carré medium
        rectangle(largeur_fenetre-395, hauteur_fenetre-300, largeur_fenetre-245, hauteur_fenetre-200, couleur='black', remplissage='black', epaisseur=6)
        rectangle(largeur_fenetre-395, hauteur_fenetre-300, largeur_fenetre-245, hauteur_fenetre-200, couleur='white', remplissage='white')
        # carré hard
        rectangle(largeur_fenetre-195, hauteur_fenetre-300, largeur_fenetre-45, hauteur_fenetre-200, couleur='black', remplissage='black', epaisseur=6)
        rectangle(largeur_fenetre-195, hauteur_fenetre-300, largeur_fenetre-45, hauteur_fenetre-200, couleur='white', remplissage='white')
        # texte
        texte(largeur_fenetre-555, hauteur_fenetre-260, "EASY", couleur="green", taille = 20, police = "Courier")
        texte(largeur_fenetre-365, hauteur_fenetre-260, "MEDIUM", couleur="orange", taille = 20, police = "Courier")
        texte(largeur_fenetre-155, hauteur_fenetre-260, "HARD", couleur="red", taille = 20, police = "Courier")
        texte(largeur_fenetre-540, hauteur_fenetre-170, "A", couleur="white", taille = 20, police = "Courier")
        texte(largeur_fenetre-335, hauteur_fenetre-170, "B", couleur="white", taille = 20, police = "Courier")
        texte(largeur_fenetre-140, hauteur_fenetre-170, "C", couleur="white", taille = 20, police = "Courier")
        while True:
            ev = donne_ev()
            tev = type_ev(ev)

            if tev == 'Touche': # gère les appuys de boutons
                if touche(ev) == "a":
                    vitesse_balle = 5 # vitesse easy
                    break
                elif touche(ev) == "b":
                    vitesse_balle = 8 # vitesse moyenne
                    break
                elif touche(ev) == "c":
                    vitesse_balle = 12 # vitesse haute
                    break
            elif tev == "ClicGauche": # gère les clics sur l'écran
                if abscisse(ev) > 40 and abscisse(ev) < 200 and ordonnee(ev) > 170 and ordonnee(ev) < 280 :
                    vitesse_balle = 5
                    break
                if abscisse(ev) > 245 and abscisse(ev) < 400 and ordonnee(ev) > 170 and ordonnee(ev) < 280 :
                    vitesse_balle = 8
                    break
                if abscisse(ev) > 450 and abscisse(ev) < 600 and ordonnee(ev) > 170 and ordonnee(ev) < 280 :
                    vitesse_balle = 12
                    break
            elif tev == 'Quitte':  # on sort de la boucle
                jouer = False # si l'utilisateur quitte, on ne lance pas le jeu
                break
            else:  # dans les autres cas, on ne fait rien
                pass
            mise_a_jour()
        break

    # permet que la direction de la balle soit différente à chaque lancement de jeu
    direction_initiale = randint(-2, 2)
    while direction_initiale == 0 : # tant que la direction initiale de la balle est égale a 0, on relance un nombre aléatoire
        direction_initiale = randint(-2, 2)
    direction_balle = (vitesse_balle, direction_initiale)  # direction initiale de la balle
    # doit se situer après le choix de difficulté

    while theme :
        # affichage des éléments
        rectangle(0, 0, largeur_fenetre, hauteur_fenetre, couleur='powderblue', remplissage='powderblue')
        rectangle(largeur_fenetre-560, hauteur_fenetre-340, largeur_fenetre-260, hauteur_fenetre-80, couleur='black', remplissage='white')
        texte(largeur_fenetre/2, hauteur_fenetre/15, "Choix du Theme", couleur="black", ancrage = "n", police = "Courier")
        texte(largeur_fenetre/4, hauteur_fenetre/5, "Appuyez sur : ", couleur="black", taille = 12, ancrage = "e", police = "Courier")
        texte(largeur_fenetre-550, hauteur_fenetre-325, "A pour le thème Classik", couleur="black", taille = 12, police = "Courier")
        texte(largeur_fenetre-550, hauteur_fenetre-275, "B pour le thème Clair", couleur="grey", taille = 12, police = "Courier")
        texte(largeur_fenetre-550, hauteur_fenetre-225, "C pour le thème Marin", couleur="blue", taille = 12, police = "Courier")
        texte(largeur_fenetre-550, hauteur_fenetre-175, "D pour le thème Sauvage", couleur="green", taille = 12, police = "Courier")
        texte(largeur_fenetre-550, hauteur_fenetre-125, "E pour le thème Football", couleur="limegreen", taille = 12, police = "Courier")
        texte(largeur_fenetre-300, hauteur_fenetre-325, """
        Note : Vérifiez bien que 
        votre touche Verr. maj est 
        désactivée avant de faire
        votre choix sinon cela ne
        fonctionnera pas.
        """, couleur="black", taille = 10, police = "Courier")
        while True:
            ev = donne_ev()
            tev = type_ev(ev)

            if tev == 'Touche': # gère les appuis de boutons
                if touche(ev) == "a": # theme classique
                    break
                elif touche(ev) == "b": # thème clair
                    couleur_fond = "white"
                    couleur_pong = "black"
                    couleur_balle = "black"
                    break
                elif touche(ev) == "c": # thème marin
                    couleur_fond = "blue"
                    couleur_pong = "mediumturquoise"
                    couleur_balle = "mediumturquoise"
                    break
                elif touche(ev) == "d": # thème sauvage
                    couleur_fond = "green"
                    couleur_pong = "brown"
                    couleur_balle = "brown"
                    break
                elif touche(ev) == "e": # thème football
                    couleur_fond = "limegreen"
                    couleur_pong = "black"
                    couleur_balle = "white"
                    break
            elif tev == 'Quitte':  # on sort de la boucle
                jouer = False # si l'utilisateur quitte, on ne lance pas le jeu
                break
            else:  # dans les autres cas, on ne fait rien
                pass
            mise_a_jour()
        break

    temps = 0 # le timer est mis à zero avant le début du jeu

    # boucle principale
    while jouer:
        # affichage des objets
        efface_tout()  # efface tous les objets
        rectangle(0, 0, largeur_fenetre, hauteur_fenetre, couleur=couleur_fond, remplissage=couleur_fond)
        if couleur_fond == "limegreen": # si le thème choisi est foot alors il y a des elements supplémentaires à afficher, c'est du bonus
            cercle(largeur_fenetre/2, hauteur_fenetre/2, 50, couleur='white', epaisseur=4)
            ligne(largeur_fenetre/2, 0, largeur_fenetre/2, hauteur_fenetre, couleur="white", epaisseur=4)
            rectangle(-10, hauteur_fenetre-300, largeur_fenetre-600, hauteur_fenetre-180, couleur="white", epaisseur=4)
            rectangle(-10, hauteur_fenetre-360, largeur_fenetre-550, hauteur_fenetre-120, couleur="white", epaisseur=4)
            rectangle(largeur_fenetre+10, hauteur_fenetre-300, largeur_fenetre-40, hauteur_fenetre-180, couleur="white", epaisseur=4)
            rectangle(largeur_fenetre+10, hauteur_fenetre-360, largeur_fenetre-90, hauteur_fenetre-120, couleur="white", epaisseur=4)
        texte(largeur_fenetre-50, hauteur_fenetre-450, "J1", couleur=couleur_pong, taille = 14, police = "Courier")
        texte(largeur_fenetre-615, hauteur_fenetre-450, "IA", couleur=couleur_pong, taille = 14, police = "Courier")
        texte(largeur_fenetre/2-5, hauteur_fenetre-450, int(temps), couleur=couleur_pong, taille = 14, police = "Courier")
        affiche_pong(position_pong1, "gauche")  # affiche la raquette gauche
        affiche_pong(position_pong2, "droite")  # affiche la raquette gauche
        affiche_balle(position_balle)  # affiche la balle
        mise_a_jour()  # met à jour l'affichage
        temps = temps + 0.065 # rajoute 0.065 au temps à chaque passage dans la boucle, de quoi imiter plus ou moins la vraie vitesse des secondes
        direction_pong2 = 0  # remet le mouvement du pong de droite à 0

        # gestion des événements
        ev = donne_ev()  # récupère les évènements clavier ou souris
        ty = type_ev(ev)  # récupère le type d'événement
        if ty == 'Quitte':
            break
        elif ty == 'Touche':  # Si c'est un événement clavier
            # print(touche(ev))
            direction_pong2 = change_direction_pong2(touche(ev))
        position_pong1 = mouvement_ordi(position_balle, position_pong1)
        position_pong2 = deplacement_pong(position_pong2, direction_pong2)
        direction_balle = detection_impact_pong(
            position_pong1, position_pong2, position_balle, direction_balle)
        direction_balle = detection_bord(position_balle, direction_balle)
        sortie = detection_sortie(position_balle)
        position_balle = deplacement_balle(position_balle, direction_balle)
        jouer = not fin_de_jeu(sortie)
        # attente avant rafraîchissement
        sleep(1/framerate)

    # Affichage fin de jeu
    affiche_victoire(sortie)
    # fermeture et sortie
    ferme_fenetre()