import pygame
import random
# importation des fichiers
from Fonctional_Joueur import *
from Fonctional_machine import *
from Smart_Machine import *
from Smart_Joueur import Reflexion_Joueur
#********************************************************
#               @Author : Josue Lubaki
#********************************************************
pygame.init() 
  
# define the RGB value for white, green, blue colour,... 
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
joueurWin = False
machineWin = False

# set the pygame window name and icon
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

# LOGIQUE DU MENU DU JEU @see ConfirmationQuitter
Control_Quit = ConfirmationQuitter(pygame,fenetre_sortie,joueurWin,machineWin)
choixUser = Control_Quit[0]
fin = Control_Quit[1]
arret = Control_Quit[2]
joueurWin = Control_Quit[3]
machineWin = Control_Quit[4]

# Connaitre le Joueur suivant à chaque tour
PlayingJoueur = True # C'est tjrs les Users qui commencent... @True
PlayingMachine = False
demande = False

# Si l'Utilisateur pointe sur n'importe quel élement non traité dans le code
mauvaisPointer = False
#attention a C de Clock
horloge = pygame.time.Clock()

# CHECKER LE CHOIX DU USER
while fin == True and arret == False:
    # Création de la fenetre de Jeu
    fenetre = pygame.display.set_mode((X,Y))
    fenetre.fill(blue_sombre) # color fond
    # Initialisation des variables pour le jeu
    case = initialiser_case()
    rec = init_variable(pygame, fenetre, blanc)
    playedCase = init_JoueurPlayedCase()
    MachineCase = init_MachinePlayedCase()
    is_running = True
    rejouer = False
    score = 0
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
            playedCase = init_JoueurPlayedCase()
            MachineCase = init_MachinePlayedCase()
            rejouer = False
            if mauvaisPointer == True:
                # Garder les cases occupées
                case[1:] = [False,False,False,False,False,False,False,False,False]
                mauvaisPointer = False

        # Si toutes les cases sont occupés, redemarrer Jeu
        if ((case[1:] == [False,False, False,False,False,False,False,False,False]) or joueurWin or machineWin):
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
                        # C'est toujours L'utilisateur qui commence
                        PlayingJoueur = True
                        PlayingMachine = False
                        joueurWin = False
                        machineWin = False
                        break
                    elif rec_t2.collidepoint(position): # veux Sortir
                        # LOGIQUE DU MENU DU JEU
                        Control_Quit = ConfirmationQuitter(pygame,fenetre,joueurWin,machineWin)
                        choixUser = Control_Quit[0]
                        fin = Control_Quit[1]
                        arret = Control_Quit[2]
                        joueurWin = Control_Quit[3]
                        machineWin = Control_Quit[4]
                        if fin == True and arret == True:
                            is_running = False
                            mauvaisPointer = False
                            score = 0
                            break
                        else:
                            mauvaisPointer = False
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
                Control_Quit = ConfirmationQuitter(pygame,fenetre,joueurWin,machineWin)
                choixUser = Control_Quit[0]
                fin = Control_Quit[1]
                arret = Control_Quit[2]
                joueurWin = Control_Quit[3]
                machineWin = Control_Quit[4]
                if fin == True and arret == True:
                    is_running = False
                    score = 0
                    break

           #Verifier si le Joueur a gagné
            maFunc = VerifierGagnant(pygame,fenetre,case,choixUser,MachineCase,playedCase,PlayingMachine,PlayingJoueur,machine_Joue,joueurWin,machineWin)
            joueurWin = maFunc[0]
            machineWin = maFunc[1]
            
            if(machineWin):
                print("La Machine a gagné")
                fin = True
                arret = False
                rejouer = True
                machineWin = False
                PlayingJoueur = True
                PlayingMachine = False
            
            if(joueurWin):
                print("Le Joueur a gagné !")
                fin = True
                arret = False
                rejouer = True
                score += 1
                joueurWin = False
                demande = True
                PlayingJoueur = True
                PlayingMachine = False
            
            # Au Tour du User de choisir une case vide
            Reflexion_User = Reflexion_Joueur(pygame,event,fenetre,case,choixUser,playedCase,
            PlayingJoueur,PlayingMachine,rec,font_info,rouge,blanc,dodger_blue,joueurWin,score)            
            # Modifier le tour | Prochain Joueur
            PlayingMachine = Reflexion_User[0] # True
            PlayingJoueur = Reflexion_User[1] # False

            # La Machine Reflechie, comment Gagner le jeu
            # ou au pire, comment contrer le Joueur
            Reflexion = Reflexion_Machine(pygame,fenetre,case,choixUser,
            MachineCase,playedCase,PlayingMachine,PlayingJoueur,machine_Joue,switching_O,switching_X,random,joueurWin,machineWin)
            # Modifier le tour | Prochain Joueur
            PlayingMachine = Reflexion[0] # False
            PlayingJoueur = Reflexion[1] # True
            joueurWin = Reflexion[2]
            machineWin = Reflexion[3]

            # Mise à jour des contenues
            pygame.display.update()      
            horloge.tick()

        # Mise à jour de tous les dessins (Rectangles)
        pygame.display.flip()      
        horloge.tick()
    else:
        Copyright(pygame,font)
        pygame.display.update()
if(fin == True and arret == True):
        Copyright(pygame,font)   
        tick = 0
        while tick < 30:
            horloge.tick(10)
            tick += 1
        pygame.quit()