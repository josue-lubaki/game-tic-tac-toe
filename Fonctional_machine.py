# Ce fihier Contient des fonctions Utiles pour la machine, comment elle reagit face au jeu
from Fonctional_Joueur import DimensionFenetre

# Reinitialisation des cases jouées par les users
def init_JoueurPlayedCase():
    c1 = False
    c2 = False
    c3 = False
    c4 = False
    c5 = False
    c6 = False
    c7 = False
    c8 = False
    c9 = False
    return [False,c1,c2,c3,c4,c5,c6,c7,c8,c9]

# Reinitialisation des cases jouées par la machine
def init_MachinePlayedCase():
    c1 = False
    c2 = False
    c3 = False
    c4 = False
    c5 = False
    c6 = False
    c7 = False
    c8 = False
    c9 = False
    return [False,c1,c2,c3,c4,c5,c6,c7,c8,c9]

# Les diffrentes Couleurs Utilisés pour les Fonctions
blue = (0, 0, 128) 
noir = (0, 0 ,0)
blanc = (220, 220, 220)
vert =  (34, 139, 34)
rouge = (165, 42, 42)
rouge_sombre = (153,0,0) 
blue_sombre = (0,51,51)
orange_sombre = (204,102,0)
orange_claire = (255,128,0)
dodger_blue = (30,144,255)

# Dessiner Symbole O
def switching_O(pygame,fenetre,indice):
    if indice == 1:
        pygame.draw.ellipse(fenetre, dodger_blue, [35,35,130,130], 30)
    elif indice == 2:
        pygame.draw.ellipse(fenetre, dodger_blue, [210,35,130,130], 30)
    elif indice == 3:
        pygame.draw.ellipse(fenetre, dodger_blue, [385,35,130,130], 30)
    elif indice == 4:
        pygame.draw.ellipse(fenetre, dodger_blue, [35,210,130,130], 30)
    elif indice == 5:
        pygame.draw.ellipse(fenetre, dodger_blue, [210,210,130,130], 30)
    elif indice == 6:
        pygame.draw.ellipse(fenetre, dodger_blue, [385,210,130,130], 30)
    elif indice == 7:
        pygame.draw.ellipse(fenetre, dodger_blue, [35,385,130,130], 30)
    elif indice == 8:
        pygame.draw.ellipse(fenetre, dodger_blue, [210,385,130,130], 30)
    elif indice == 9:
        pygame.draw.ellipse(fenetre, dodger_blue, [385,385,130,130], 30)
    else:
        print("Je ne sais pas sur quelle case dessinée")

# Dessiner symbole X
def switching_X(pygame,fenetre,indice):
    if indice == 1:
        pygame.draw.line(fenetre, rouge,[35,25],[165,174], 20)
        pygame.draw.line(fenetre, rouge,[165,25],[35,174], 20)
    elif indice == 2:
        pygame.draw.line(fenetre, rouge,[210,25],[339,174], 20)
        pygame.draw.line(fenetre, rouge,[339,25],[210,174], 20)
    elif indice == 3:
        pygame.draw.line(fenetre, rouge,[385,25],[514,174], 20)
        pygame.draw.line(fenetre, rouge,[515,25],[384,174], 20)
    elif indice == 4:
        pygame.draw.line(fenetre, rouge,[35,200],[165,349], 20)
        pygame.draw.line(fenetre, rouge,[165,200],[35,349], 20)
    elif indice == 5:
        pygame.draw.line(fenetre, rouge,[210,200],[339,349], 20)
        pygame.draw.line(fenetre, rouge,[339,200],[210,349], 20)
    elif indice == 6:
        pygame.draw.line(fenetre, rouge,[385,200],[514,349], 20)
        pygame.draw.line(fenetre, rouge,[514,200],[384,349], 20)
    elif indice == 7:
        pygame.draw.line(fenetre, rouge,[35,375],[164,524], 20)
        pygame.draw.line(fenetre, rouge,[164,375],[35,524], 20)
    elif indice == 8:
        pygame.draw.line(fenetre, rouge,[210,375],[339,524], 20)
        pygame.draw.line(fenetre, rouge,[339,375],[210,524], 20)
    elif indice == 9:
        pygame.draw.line(fenetre, rouge,[385,375],[514,524], 20)
        pygame.draw.line(fenetre, rouge,[514,375],[384,524], 20)
    else:
        print("Je ne sais pas sur quelle case dessinée")

def machine_Joue(pygame,fenetre,case,i,choixUser,PlayingMachine,PlayingJoueur):
    _break = False
    if case[i] == True:
        if choixUser == "X":
            switching_O(pygame,fenetre,i)
            case[i] = False
            PlayingMachine = False
            PlayingJoueur = True
            _break = True
        else:
            switching_X(pygame,fenetre,i)
            case[i] = False
            PlayingMachine = False
            PlayingJoueur = True
            _break = True
    return [PlayingMachine,PlayingJoueur,_break]

def Copyright(pygame,font):
    # Dimension fenetre
    dimension = DimensionFenetre()
    X = dimension[0]
    Y = dimension[1]
    fenetre_quit = pygame.display.set_mode((X,Y)) # definition fenetre_quit
    # Coder ici | User veut partir | text de confirmation
    fenetre_quit.fill(blue_sombre) # color fond
    # TEXT
    text_sortie = font.render('Copyright 2020 - Josue Lubaki', True, noir ,orange_sombre)
    # Allouer l'espace necessaire pour le text
    textRect_Sortie = text_sortie.get_rect() 
    # Positionner les Textes dans la Page
    textRect_Sortie.center = (X // 2, Y // 2)
    fenetre_quit.blit(text_sortie, textRect_Sortie)
    # Mise à jour des contenues
    pygame.display.update()