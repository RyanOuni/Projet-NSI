from davistk import image
from davistk import mise_a_jour, type_ev, ferme_fenetre
from davistk import touche, cree_fenetre, efface_tout, donne_ev
from davistk import fleche, ligne
from davistk import texte
from davistk import rectangle
from davistk import attend_ev
from davistk import abscisse
from davistk import ordonnee
from time import sleep
from random import randint
from math import sqrt
from davistk import attend_clic_gauche

# dimensions du jeu
largeur_route = 100
largeur_fenetre = 640
hauteur_fenetre = 480


def creer_route(position_route):
    ''' Ne pas modifier. Permet de créer une route initiale.
    Une route est formée de 4 valeurs: 3 abscisses de points
    séparés en ordonnée par une hauteur d'écran et l'ordonnée du point
    du bas.
    Parameters:
        position_route (int): position du point du bas
    Returns:
        (int, int, int, int):   abscisse du point du bas,
                                abscisse du point du milieu,
                                abscisse du point du haut,
                                ordonnée du point du bas
    '''
    x_bas_gauche = position_route
    x_milieu_gauche = randint(50, largeur_fenetre - largeur_route - 50)
    x_haut_gauche = randint(50, largeur_fenetre - largeur_route - 50)
    return x_bas_gauche, x_milieu_gauche, x_haut_gauche, hauteur_fenetre


def affiche_route(route):
    ''' Ne pas modifier. Affiche la route à partir de l'information route
    composée de 4 valeurs: 3 abscisses de points séparés en ordonnée par
    une hauteur d'écran et l'ordonnée du point du bas.
    Parameters:
        route (int, int, int, int): abscisse du point du bas,
                                    abscisse du point du milieu,
                                    abscisse du point du haut,
                                    ordonnée du point du bas
    '''
    x_bas_gauche, x_milieu_gauche, x_haut_gauche, y_bas = route
    ligne(x_bas_gauche, y_bas, x_milieu_gauche, y_bas
          - hauteur_fenetre, epaisseur=2, couleur='white')
    ligne(x_bas_gauche + largeur_route, y_bas, x_milieu_gauche
          + largeur_route, y_bas - hauteur_fenetre, epaisseur=2, couleur='white')
    ligne(x_milieu_gauche, y_bas - hauteur_fenetre,
          x_haut_gauche, y_bas - 2 * hauteur_fenetre, epaisseur=2, couleur='white')
    ligne(x_milieu_gauche + largeur_route, y_bas - hauteur_fenetre, x_haut_gauche
          + largeur_route, y_bas - 2 * hauteur_fenetre, epaisseur=2, couleur='white')
    mise_a_jour()


def avance_route(route, vitesse):
    ''' Ne pas modifier. Permet de faire avancer la route à la vitesse de la
    voiture.
    On augmente donc l'ordonnée du point du bas de vitesse.
    Si le point du bas est trop bas, cela signifie que le point du haut devient
    visible, on crée un nouveau point en haut.
    Parameters:
        route (int, int, int, int): abscisse du point du bas,
                                    abscisse du point du milieu,
                                    abscisse du point du haut,
                                    ordonnée du point du bas
        vitesse (int): nombre de pixels défilant à chaque mise à jour du
        graphique.
    Returns:
        (int, int, int, int):   abscisse du point du bas,
                                abscisse du point du milieu,
                                abscisse du point du haut,
                                ordonnée du point du bas
    '''
    x_bas_gauche, x_milieu_gauche, x_haut_gauche, y_bas = route
    y_bas += vitesse
    if y_bas > 2 * hauteur_fenetre:
        x_bas_gauche = x_milieu_gauche
        x_milieu_gauche = x_haut_gauche
        x_haut_gauche = randint(50, largeur_fenetre - largeur_route - 50)
        y_bas = hauteur_fenetre
    return x_bas_gauche, x_milieu_gauche, x_haut_gauche, y_bas


def creer_voiture(route):
    ''' Ne pas modifier. Permet de créer la voiture au milieu de
    la route, aux 3/4 de l'écran en partant du haut, dans la direction
    de la route (inverse du coefficient directeur de la droite)
    Parameters:
        route (int, int, int, int): abscisse du point du bas,
                                    abscisse du point du milieu,
                                    abscisse du point du haut,
                                    ordonnée du point du bas
    Returns:
        (float, float, float):  abscisse de la voiture,
                                ordonnée de la voiture,
                                direction de la voiture
    '''
    x_bas_gauche, x_milieu_gauche, x_haut_gauche, y_bas = route
    x_voiture = (3 * x_bas_gauche + x_milieu_gauche) / 4 + largeur_route / 2
    y_voiture = 3 / 4 * y_bas
    direction = (x_bas_gauche - x_milieu_gauche) / (y_bas)
    return x_voiture, y_voiture, direction


def affiche_voiture(voiture):
    ''' Ne pas modifier. Affiche la voiture comme une flêche rouge
    dans la bonne direction.
    Parameters:
        voiture (float, float, float):  abscisse de la voiture,
                                        ordonnée de la voiture,
                                        direction de la voiture
    '''
    x_voiture, y_voiture, direction = voiture
    fleche(x_voiture, y_voiture, x_voiture - direction / sqrt(1 + direction ** 2),
           y_voiture - 1 / sqrt(1 + direction ** 2), epaisseur=2, couleur='red')
    image(x_voiture,y_voiture,'Race/voiture.png',ancrage='center',tag='voiture1')

def affiche_menu1(Tex1, Tex2, Tex3, Tex4, x1, y1, x2, y2, x3, y3, x4, y4):
    '''Permet d afficher un menu avec unes instruction en haut un boutton adroite et a gauche et un boutton en bas.
    Parametrs:
            Tex1:Un texte qu on veut afficher
            Tex2:Un texte qu on veut afficher
            Tes3:Un texte qu on veut afficher
            Tex4:Un texte qu on veut afficher
            x1 et y1:abscisse et ordonnée du Tex1
            x2 et y2:abscisse et ordonnée du Tex2
            x3 et y3:abscisse et ordonnée du Tex3
            x4 et y4:abscisse et ordonnée du Tex4
    '''
    image(0,0,'Race/modemenu.png',ancrage='nw',tag='mode_menu')
    rectangle(30, 25, 610, 85, couleur='black', remplissage='', epaisseur=1, tag='')
    rectangle(30, 250, 250, 350, couleur='black', remplissage='', epaisseur=1, tag='')
    texte(x2,y2,Tex2,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')
    rectangle(390, 250, 610, 350, couleur='black', remplissage='', epaisseur=1, tag='')
    texte(x3,y3,Tex3,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')
    rectangle(30, 400, 610, 460, couleur='black', remplissage='', epaisseur=1, tag='')
    texte(x4,y4,Tex4,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')
    image(0,0,'Race/modemenu.png',ancrage='nw',tag='mode_menu')
    mise_a_jour()

def affiche_menu2(Tex1, Tex2, Tex3, Tex4, x1, y1, x2, y2, x3, y3, x4, y4):
    image(0,0,'Race/difficultéemenu.png',ancrage='nw',tag='difficulté')
    rectangle(30, 25, 610, 85, couleur='black', remplissage='', epaisseur=1, tag='')
    texte(x1,y1,Tex1,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')
    rectangle(30, 250, 250, 350, couleur='black', remplissage='', epaisseur=1, tag='')
    texte(x2,y2,Tex2,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')
    rectangle(390, 250, 610, 350, couleur='black', remplissage='', epaisseur=1, tag='')
    texte(x3,y3,Tex3,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')
    rectangle(30, 400, 610, 460, couleur='black', remplissage='', epaisseur=1, tag='')
    texte(x4,y4,Tex4,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')
    image(0,0,'Race/difficultéemenu.png',ancrage='nw',tag='mode_difficulté')
    mise_a_jour()

def choix_clic_gauche():
    '''Peremt de detecter un clic gauche a certaine coordonnéé.C ets coordonnée sont celle des boutton
    de la fonction affiche_menu.
    Returns:
            int(1;2 ou 3): sur quelle boutton le joueur a clicé.
    '''
    cpt = 0
    cpt_choix = 0
    while cpt == 0:
        Choix = attend_ev()
        ty_choix = type_ev(Choix)
        if abscisse(Choix) >= 30 and abscisse(Choix) <= 250 and ordonnee(Choix) >= 250 and ordonnee(Choix) <= 350 and ty_choix == 'ClicGauche':#Si mode normale choisis
            cpt_choix +=1
            cpt += 1
        elif abscisse(Choix) >= 390 and abscisse(Choix) <= 610 and ordonnee(Choix) >= 250 and ordonnee(Choix) <= 350 and ty_choix == 'ClicGauche':#si mode croissant choisis
            cpt_choix += 2
            cpt += 1
        elif abscisse(Choix) >= 30 and abscisse(Choix) <= 610 and ordonnee(Choix) >= 400 and ordonnee(Choix) <= 460 and ty_choix == 'ClicGauche':
            cpt_choix += 3
            cpt += 1
    return cpt_choix

def deplace(voiture, vitesse):
    ''' Permet de déplacer la voiture. Soustrait à l'abscisse de la voiture la
    vitesse multiplié par la direction.
    Parameters:
        voiture (float, float, float):  abscisse de la voiture,
                                        ordonnée de la voiture,
                                        direction de la voiture
    Returns:
        (float, float, float):  abscisse de la voiture,
                                ordonnée de la voiture,
                                direction de la voiture
    '''
    x_voiture, y_voiture, direction = voiture
    x_voiture= x_voiture-(vitesse*direction)
    return x_voiture, y_voiture, direction


def change_direction(voiture, vitesse, touche):
    ''' Permet de changer la direction et la vitesse de la voiture avec
    le clavier et que la vitesse est compris dans l intervale [0;10].
    Si on appuie sur la touche du "Up", on ajoute 1 à la vitesse.
    Si on appuie sur la touche du "Down", on retire 1 à la vitesse.
    Si on appuie sur la touche du "Right", on retire 0.1 à la direction.
    Si on appuie sur la touche du "Left", on ajoute 0.1 à la direction.
    Parameters:
        voiture (float, float, float):  abscisse de la voiture,
                                        ordonnée de la voiture,
                                        direction de la voiture
        vitesse (int): vitesse de la x_voiture
        touche (str): nom de la touche pressée
    Returns:
        voiture (float, float, float):  abscisse de la voiture,
                                        ordonnée de la voiture,
                                        direction de la voiture
        vitesse (int): vitesse de la x_voiture
    '''
    x_voiture, y_voiture, direction = voiture
    if touche == 'Up' and vitesse < 10:
        vitesse += 1
    elif touche == "Down" and vitesse > 0:
        vitesse -= 1
    elif touche == "Right":
        direction -= 0.1
    else:
        direction +=0.1
    voiture = x_voiture, y_voiture, direction
    return voiture, vitesse

def change_direction_sans_vitesse(voiture, touche):
    ''' Permet de changer la direction et la vitesse de la voiture avec
    le clavier et que la vitesse est compris dans l intervale [0;10].
    Si on appuie sur la touche du "Up", on ajoute 1 à la vitesse.
    Si on appuie sur la touche du "Down", on retire 1 à la vitesse.
    Si on appuie sur la touche du "Right", on retire 0.1 à la direction.
    Si on appuie sur la touche du "Left", on ajoute 0.1 à la direction.
    Parameters:
        voiture (float, float, float):  abscisse de la voiture,
                                        ordonnée de la voiture,
                                        direction de la voiture
        vitesse (int): vitesse de la x_voiture
        touche (str): nom de la touche pressée
    Returns:
        voiture (float, float, float):  abscisse de la voiture,
                                        ordonnée de la voiture,
                                        direction de la voiture
        vitesse (int): vitesse de la x_voiture
    '''
    x_voiture, y_voiture, direction = voiture
    if touche == "Right":
        direction -= 0.1
    else:
        direction +=0.1
    voiture = x_voiture, y_voiture, direction
    return voiture, vitesse

def detection_impact(route, voiture):
    ''' Ne pas modifier. Permet de détecter la colision avec bord de la route.
    Parameters:
        route (int, int, int, int): abscisse du point du bas,
                                    abscisse du point du milieu,
                                    abscisse du point du haut,
                                    ordonnée du point du bas
        voiture (float, float, float):  abscisse de la voiture,
                                        ordonnée de la voiture,
                                        direction de la voiture
    Returns:
        (bool): True si il y a eu collision, False sinon
    '''
    x_voiture, y_voiture, direction = voiture
    x_bas_gauche, x_milieu_gauche, x_haut_gauche, y_bas = route
    coef_directeur_bas = (x_milieu_gauche - x_bas_gauche)/(- hauteur_fenetre)
    coef_directeur_haut = (x_haut_gauche - x_milieu_gauche)/(- hauteur_fenetre)
    if y_bas < (1 + 3/4) * hauteur_fenetre:
        if x_voiture < x_bas_gauche + coef_directeur_bas * (y_voiture - y_bas) or x_voiture > x_bas_gauche + coef_directeur_bas * (y_voiture - y_bas) + largeur_route:
            return True
        else:
            return False
    else:
        if x_voiture < x_milieu_gauche + coef_directeur_haut * (y_voiture - y_bas + hauteur_fenetre) or x_voiture > x_milieu_gauche + coef_directeur_haut * (y_voiture - y_bas + hauteur_fenetre) + largeur_route:
            return True
        else:
            return False

def affiche_menu_victoire():
    image(0,0,'Race/menudevictoire.png',ancrage='nw')

def affiche_victoire():
    ''' Fonction permettant de gérer graphiquement la fin de jeu
    Parameters:
        ...
    Returns:
        ...
    '''
    efface_tout()
    affiche_menu_victoire()

def affiche_menu_défaite():
    image(0,0,'Race/gameover.png',ancrage='nw')




# programme principal
if __name__ == "__main__":
    # initialisation du jeu
    framerate = 20    # taux de rafraîchissement du jeu en images/s
    direction_voiture = (0, -1)  # direction initiale de la voiture
    position_route = 100  # position initiale de la balle
    cree_fenetre(largeur_fenetre, hauteur_fenetre)
    vitesse = 3  # Vitesse initiale
    route = creer_route(position_route)
    voiture = creer_voiture(route)
    cpt_score = 0
    jouer = True
    #Menu Mode
    affiche_menu1("Choisis un mode","Mode normal","Mode croissant ","Quitter",210.0,40.0,50.0,285.0,393.0,285.0,272.0,415.0)#our choisir cordoner des texte das creation fonction
    cpt_choix_mode = choix_clic_gauche() 
    if cpt_choix_mode == 3:
        ferme_fenetre() 

    #menu difficulté
    efface_tout()
    affiche_menu2("Choisis une difficultée","Facil","Dure","Quitter",172.0,40.0,100.0,285.0,460.0,285.0,272.0,415.0)
    cpt_choix_difficulté = choix_clic_gauche()
    
    if cpt_choix_difficulté == 3:
        ferme_fenetre()
    elif cpt_choix_difficulté == 1:
        score_gagner = 15000 #Le score pour gagner
    else:
        score_gagner = 25000

    # boucles principales
    if cpt_choix_mode == 1:# si mode normal choisi 
        while jouer:
        # affichage des objets
            affiche_voiture(voiture)
            efface_tout()  # efface tous les objets
            image(0,0,'Race/route.png',ancrage='nw')
            str(vitesse)
            texte(610.0,10.0,vitesse,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')#affiche la vitesse en haut a droite
            int(vitesse)
            texte(20.0,10.0,cpt_score,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')#affiche le score en haut a gauche
            affiche_route(route)  # affiche la route
            affiche_voiture(voiture)  # affiche la voiture
            mise_a_jour()  # met à jour l'affichage

            # gestion des événements
            ev = donne_ev()  # récupère les évènements clavier ou souris
            ty = type_ev(ev)  # récupère le type d'événement
            if ty == 'Quitte':
                break
            elif ty == 'Touche':  # Si c'est un événement clavier
                # print(touche(ev))
                voiture, vitesse = change_direction(voiture, vitesse, touche(ev))
            route = avance_route(route, vitesse)
            voiture = deplace(voiture, vitesse)
            if vitesse != 0:#sert a modifier le scor
                cpt_score += vitesse
            crash = detection_impact(route, voiture)
            jouer = not crash
            if crash == True:
                affiche_menu_défaite()
                break
            ...  # à modifier
            # attente avant rafraîchissement
            sleep(1 / framerate)
            if cpt_score<score_gagner:#permet de savoir si le score et egale au score_ganer pour savoir si il faut afficher la victoire
                continue        
            elif cpt_score>score_gagner:
                efface_tout()
                affiche_victoire()
                break 
        attend_clic_gauche()
        ferme_fenetre()
    elif cpt_choix_mode == 2:#si mode arcade choisi
        while jouer:
        # affichage des objets
            affiche_voiture(voiture)  # affiche la voiture
            efface_tout()  # efface tous les objets
            image(0,0,'Race/route.png',ancrage='nw')
            str(vitesse)
            texte(610.0,10.0,vitesse,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')#affiche la vitesse en haut a droite
            int(vitesse)
            texte(20.0,10.0,cpt_score,couleur='red',ancrage='nw', police='Helvetica', taille=24, tag='')#affiche le score en haut a gauche
            affiche_route(route)  # affiche la route
            affiche_voiture(voiture)  # affiche la voiture
            mise_a_jour()  # met à jour l'affichage

            # gestion des événements
            ev = donne_ev()  # récupère les évènements clavier ou souris
            ty = type_ev(ev)  # récupère le type d'événement
            if ty == 'Quitte':
                break
            elif ty == 'Touche':  # Si c'est un événement clavier
                # print(touche(ev))
                voiture, vitesse = change_direction_sans_vitesse(voiture, touche(ev))
            route = avance_route(route, vitesse)
            voiture = deplace(voiture, vitesse)
            if vitesse != 0:
                cpt_score += vitesse
            crash = detection_impact(route, voiture)
            jouer = not crash
            if cpt_score >= 10**vitesse:#augmente la vittesse de 1 si 10**vitesse est atteint
                vitesse += 1
            if crash == True:
                affiche_menu_défaite()
                break
                
            # attente avant rafraîchissement
            sleep(1 / framerate)
            if cpt_score<score_gagner:
                continue        
            elif cpt_score>score_gagner:
                efface_tout()
                affiche_victoire() 
                break
        attend_clic_gauche()
        ferme_fenetre()
