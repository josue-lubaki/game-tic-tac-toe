import pygame
import random
# importation du fichier Fonctional (contenant les Fonctions)
from Fonctional import *
 
pygame.init() 
  
# define the RGB value for white, 
#  green, blue colour . 
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
  
# assigning values to X and Y variable 
dimension = DimensionFenetre()
X = dimension[0]
Y = dimension[1]
  
# create the display surface object 
# of specific dimension..e(X, Y).
fenetre_sortie = pygame.display.set_mode((X,Y))


# set the pygame window name 
pygame.display.set_caption('TIC-TAC-TOE')
icon = pygame.image.load("image/tic-tac-toe_32.png")
pygame.display.set_icon(icon)

# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
font_titre = pygame.font.Font('freesansbold.ttf', 38)
font = pygame.font.Font('freesansbold.ttf', 32) 
font_info = pygame.font.Font('freesansbold.ttf', 24) 

# LOGIQUE DU MENU DU JEU
Control_Quit = ConfirmationQuitter(pygame,fenetre_sortie)
choixUser = Control_Quit[0]
fin = Control_Quit[1]
arret = Control_Quit[2]

# Connaitre le Joueur suivant à chaque tour
PlayingJoueur = True # C'est tjrs les Users qui commencent...
PlayingMachine = False

mauvaisPointer = False
#attention a C de Clock
horloge = pygame.time.Clock()

# CHECKER LE CHOIX DU USER (code ici) 
while fin == True and arret == False:
    # Création de la fenetre de Jeu
    fenetre = pygame.display.set_mode((X,Y))
    fenetre.fill(blue_sombre) # color fond
    # Initialisation des variables pour le jeu
    case = initialiser_case()
    rec = init_variable(pygame, fenetre, blanc)
    is_running = True
    rejouer = False

    # Lancement du jeu (Partie choix des cases)
    while is_running == True:
        # Condition de Redemarrage | Nouvelle Partie
        if rejouer == True:
            # Création de la fenetre de Jeu
            fenetre = pygame.display.set_mode((X,Y))
            fenetre.fill(blue_sombre) # color fond
            # Initialisation des variables pour le jeu
            case = initialiser_case()
            rec = init_variable(pygame, fenetre, blanc)
            rejouer = False
            if mauvaisPointer == True:
                case[1:] = [False,False,False,False,False,False,False,False,False]
                mauvaisPointer = False

        # Si toutes les cases sont occupés, redemarrer Jeu
        if (case[1:] == [False,False, False,False,False,False,False,False,False]):
            for event in pygame.event.get():    
                # Creer une interface de confirmation | Continuer ou pas
                pygame.display.update()
                fenetre = pygame.display.set_mode((X,Y)) # definition fenetre
                # Coder ici | User veut partir | text de confirmation
                fenetre.fill(blue_sombre) # color fond
                # TEXT
                text_sortie = font.render('Voulez-vous jouer de nouveau ?', True, orange_sombre)
                text_3 = font_titre.render('OUI', True, dodger_blue, noir)
                text_4 = font_titre.render('NON', True, rouge_sombre,noir)
                # Allouer l'espace necessaire pour le text
                textRect_Sortie = text_sortie.get_rect() 
                rec_t1 = pygame.draw.rect(fenetre, noir, (150,250,100,80))
                rec_t2 = pygame.draw.rect(fenetre, noir, (300,250,100,80))
                # Positionner les Textes dans la Page
                textRect_Sortie.center = (X // 2, Y // 3)
                rec_t1.center = (215, 310) # OUI
                rec_t2.center = (357, 310) # NON 
                
                fenetre.blit(text_sortie, textRect_Sortie)
                fenetre.blit(text_3, rec_t1) 
                fenetre.blit(text_4, rec_t2)
                # Verifier le clic de l'utilisateur
                if event.type == pygame.MOUSEBUTTONUP:
                    position = pygame.mouse.get_pos()
                    print(position, " - Rejouer")
                    # Condition de sortie | Fin du Jeu
                    if rec_t1.collidepoint(position): # Veux Jouer
                        fin = True
                        arret = False
                        is_running = True
                        rejouer = True
                        mauvaisPointer = False
                        break
                    elif rec_t2.collidepoint(position): # veux Sortir
                        is_running = False
                        fin = True
                        arret = True
                        mauvaisPointer = False
                        break
                    else: # Au cas où on cliquait sur un autre endroit que Oui ou Non
                        fin = True
                        arret = False
                        is_running = True
                        rejouer = True
                        mauvaisPointer = True
                        break
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
            event.key == pygame.K_q)):
                # Quitter le jeu sur QUIT [X] ou la touche "Q"
                is_running = False
                # LOGIQUE DU MENU DU JEU
                Control_Quit = ConfirmationQuitter(pygame,fenetre)
                choixUser = Control_Quit[0]
                fin = Control_Quit[1]
                arret = Control_Quit[2]
                if fin == True and arret == True:
                    is_running = False
                    break
            
            # S'il existe au moins une case vide | Tour Joeur
            if ((case[1] == True or case[2] == True or case[3] == True or case[4] == True 
            or case[5] == True or case[6] == True or case[7] == True or case[8] == True or
            case[9] == True) and PlayingJoueur == True and PlayingMachine == False):
                # Affichage du choix de l'Utilisateur
                texte = font_info.render('Vous êtes --> '+ choixUser,True,noir,orange_sombre) 
                # create a rectangular object for the 
                # text surface object 
                textRect = texte.get_rect()
                # copying the text surface object 
                # to the display surface object 
                fenetre.blit(texte, textRect) 
                UserPlayed = False # l'Utilisateur n'a pas encore joué
                #LOGIQUE DU JEU
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos, " - Choix Rectangle")

                    # rec[1] à rec[9] correspondent aux rectangles
                    if rec[1].collidepoint(pos) and case[1]:
                        if choixUser == "X":
                                pygame.draw.line(fenetre, rouge,[35,25],[165,174], 20)
                                pygame.draw.line(fenetre, rouge,[165,25],[35,174], 20)
                        else:
                            # (100,100) le centre du circle, 50 rayon )        
                            pygame.draw.ellipse(fenetre, dodger_blue, [35,35,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[1] = False
                    
                    if rec[2].collidepoint(pos) and case[2]:
                        if choixUser == "X":
                            pygame.draw.line(fenetre, rouge,[210,25],[339,174], 20)
                            pygame.draw.line(fenetre, rouge,[339,25],[210,174], 20)
                        else:
                            # on ajoute 100 + 175 =275
                            pygame.draw.ellipse(fenetre, dodger_blue, [210,35,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[2] = False
                    
                    if rec[3].collidepoint(pos) and case[3] :
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[385,25],[514,174], 20)
                                pygame.draw.line(fenetre, rouge,[515,25],[384,174], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [385,35,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[3] = False
                            
                    if rec[4].collidepoint(pos) and case[4] :
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[35,200],[165,349], 20)
                                pygame.draw.line(fenetre, rouge,[165,200],[35,349], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [35,210,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[4] = False
                        
                    if rec[5].collidepoint(pos) and case[5]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[210,200],[339,349], 20)
                                pygame.draw.line(fenetre, rouge,[339,200],[210,349], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [210,210,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[5] = False
                    
                    if rec[6].collidepoint(pos) and case[6]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[385,200],[514,349], 20)
                                pygame.draw.line(fenetre, rouge,[514,200],[384,349], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [385,210,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[6] = False
                        
                    if rec[7].collidepoint(pos) and case[7]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[35,375],[164,524], 20)
                                pygame.draw.line(fenetre, rouge,[164,375],[35,524], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [35,385,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[7] = False
                    
                    if rec[8].collidepoint(pos) and case[8]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[210,375],[339,524], 20)
                                pygame.draw.line(fenetre, rouge,[339,375],[210,524], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [210,385,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[8] = False

                    if rec[9].collidepoint(pos) and case[9]:
                        if choixUser == "X":
                            if rec[0] == True :
                                pygame.draw.line(fenetre, rouge,[385,375],[514,524], 20)
                                pygame.draw.line(fenetre, rouge,[514,375],[384,524], 20)
                        else:
                            pygame.draw.ellipse(fenetre, dodger_blue, [385,385,130,130], 30)
                        PlayingMachine = True # à la machine de jouer
                        PlayingJoueur = False
                        case[9] = False
            
            pygame.display.update()
            #20 images par seconde, 10 moin vite que 20        
            horloge.tick()

            # S'il existe au moins une case vide | Tour Machine
            if ((case[1] == True or case[2] == True or case[3] == True or case[4] == True 
                or case[5] == True or case[6] == True or case[7] == True or case[8] == True or
                case[9] == True) and PlayingMachine == True and PlayingJoueur == False):
                    listeIndiceCaseVide = []
                    listeIndiceRandomise = []
                    a = 1
                    for a in range(len(case)):
                        if(case[a] == True):
                            listeIndiceCaseVide.append(a) # indice : 2,4,7...
                    while PlayingMachine == True :
                        # Randomiser la liste
                        while len(listeIndiceCaseVide) != 0 :
                            tailleListe = len(listeIndiceCaseVide)
                            chiffreRandom = random.randint(0,tailleListe-1)
                            IndiceRandom = listeIndiceCaseVide[chiffreRandom] # 2,4,7...
                            listeIndiceRandomise.append(IndiceRandom)
                            del listeIndiceCaseVide[chiffreRandom]
                        # Demander à la machine de Jouer
                        # Prendre une case au hasard et coché
                        if (len(listeIndiceRandomise) != 0):
                            indiceCaseRandom = random.choice(listeIndiceRandomise)
                            # Verifier si la case et occupé ou pas
                            if case[indiceCaseRandom] == True:
                                if choixUser == "X":
                                    if indiceCaseRandom == 1:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [35,35,130,130], 30)
                                    elif indiceCaseRandom == 2:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [210,35,130,130], 30)
                                    elif indiceCaseRandom == 3:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [385,35,130,130], 30)
                                    elif indiceCaseRandom == 4:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [35,210,130,130], 30)
                                    elif indiceCaseRandom == 5:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [210,210,130,130], 30)
                                    elif indiceCaseRandom == 6:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [385,210,130,130], 30)
                                    elif indiceCaseRandom == 7:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [35,385,130,130], 30)
                                    elif indiceCaseRandom == 8:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [210,385,130,130], 30)
                                    elif indiceCaseRandom == 9:
                                        pygame.draw.ellipse(fenetre, dodger_blue, [385,385,130,130], 30)
                                    else:
                                        print("Je ne sais pas sur quelle case dessinée")

                                    case[indiceCaseRandom] = False
                                    PlayingMachine = False
                                    PlayingJoueur = True
                                    break
                                elif choixUser == "O":
                                    if indiceCaseRandom == 1:
                                        pygame.draw.line(fenetre, rouge,[35,25],[165,174], 20)
                                        pygame.draw.line(fenetre, rouge,[165,25],[35,174], 20)
                                    elif indiceCaseRandom == 2:
                                        pygame.draw.line(fenetre, rouge,[210,25],[339,174], 20)
                                        pygame.draw.line(fenetre, rouge,[339,25],[210,174], 20)
                                    elif indiceCaseRandom == 3:
                                        pygame.draw.line(fenetre, rouge,[385,25],[514,174], 20)
                                        pygame.draw.line(fenetre, rouge,[515,25],[384,174], 20)
                                    elif indiceCaseRandom == 4:
                                        pygame.draw.line(fenetre, rouge,[35,200],[165,349], 20)
                                        pygame.draw.line(fenetre, rouge,[165,200],[35,349], 20)
                                    elif indiceCaseRandom == 5:
                                        pygame.draw.line(fenetre, rouge,[210,200],[339,349], 20)
                                        pygame.draw.line(fenetre, rouge,[339,200],[210,349], 20)
                                    elif indiceCaseRandom == 6:
                                        pygame.draw.line(fenetre, rouge,[385,200],[514,349], 20)
                                        pygame.draw.line(fenetre, rouge,[514,200],[384,349], 20)
                                    elif indiceCaseRandom == 7:
                                        pygame.draw.line(fenetre, rouge,[35,375],[164,524], 20)
                                        pygame.draw.line(fenetre, rouge,[164,375],[35,524], 20)
                                    elif indiceCaseRandom == 8:
                                        pygame.draw.line(fenetre, rouge,[210,375],[339,524], 20)
                                        pygame.draw.line(fenetre, rouge,[339,375],[210,524], 20)
                                    elif indiceCaseRandom == 9:
                                        pygame.draw.line(fenetre, rouge,[385,375],[514,524], 20)
                                        pygame.draw.line(fenetre, rouge,[514,375],[384,524], 20)
                                    else:
                                        print("Je ne sais pas sur quelle case dessinée")

                                    case[indiceCaseRandom] = False
                                    PlayingMachine = False
                                    PlayingJoueur = True
                                    break
                                else:
                                    PlayingMachine = True
                                    print("Je ne sais pas sur quelle case dessinée")
        pygame.display.flip()
        #20 images par seconde, 10 moin vite que 20        
        horloge.tick()
    else:
        pass
if(fin == True and arret == True):
    pygame.quit()