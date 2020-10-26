import pygame
from Fonctional import *
 
pygame.init() 
  
# define the RGB value for white, 
#  green, blue colour . 
blue = (0, 0, 128) 
noir = (0, 0 ,0)
blanc = (255, 255, 255)
vert =  (0, 255, 0)
rouge = (255, 0, 0)
rouge_sombre = (153,0,0) 
blue_sombre = (0,51,51)
orange_sombre = (204,102,0)
orange_claire = (255,128,0)
  
# assigning values to X and Y variable 
X = 550
Y = 550
  
# create the display surface object 
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y ))
 
# set the pygame window name 
pygame.display.set_caption('TIC-TAC-TOE')
icon = pygame.image.load("tic-tac-toe_32.png")
pygame.display.set_icon(icon)

# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
font_titre = pygame.font.Font('freesansbold.ttf', 38)
font = pygame.font.Font('freesansbold.ttf', 32) 
font_info = pygame.font.Font('freesansbold.ttf', 24) 
  
# create a text suface object, 
# on which text is drawn on it. 
text = font_titre.render('TIC - TAC - TOE', True, orange_claire)
text_2 = font.render('Faites le Choix de votre Symbole', True, orange_sombre)

# create a rectangular object for the 
# text surface object 
textRect = text.get_rect() 
textRect_2 = text_2.get_rect() 

#attention a C de Clock
horloge = pygame.time.Clock()

# set the center of the rectangular object. 
textRect.center = (X // 2, Y // 5) 
textRect_2.center = (X // 2, Y // 2)

fin = False
choixUser = "Y" 
arret = False
# LOGIQUE DU MENU DU JEU
while fin == False: 
    # completely fill the surface object 
    # with white color 
    display_surface.fill(blue_sombre)
    # Creation de deux cases pour le choix du symbole
    rec_1 = pygame.draw.rect(display_surface, blanc, (100,300,150,150))
    rec_2 = pygame.draw.rect(display_surface, blanc, (275,300,150,150))

    # copying the text surface object 
    # to the display surface object  
    # at the center coordinate. 
    display_surface.blit(text, textRect) 
    display_surface.blit(text_2, textRect_2) 
    
    go_out = True
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
            event.key == pygame.K_q): 
            arret = True # Sortit du jeu sans avoir joué | partant du menu
            go_out = True

        if arret == True and go_out == True:
            pygame.display.update()
            fenetre_sortie = pygame.display.set_mode((X,Y)) # definition fenetre
            # Coder ici | User veut partir | text de confirmation
            fenetre_sortie.fill(blue_sombre) # color fond
            # TEXT
            text_sortie = font.render('Voulez-vous Quitter la Partie ?', True, orange_sombre)
            text_3 = font_titre.render('OUI', True, vert, noir)
            text_4 = font_titre.render('NON', True, rouge_sombre,noir)
            # Allouer l'espace necessaire pour le text
            textRect_Sortie = text_sortie.get_rect() 
            rec_t1 = pygame.draw.rect(fenetre_sortie, noir, (150,250,100,80))
            rec_t2 = pygame.draw.rect(fenetre_sortie, noir, (300,250,100,80))
            # Positionner les Textes dans la Page
            textRect_Sortie.center = (X // 2, Y // 3)
            rec_t1.center = (215, 310) # OUI
            rec_t2.center = (357, 310) # NON 
            
            fenetre_sortie.blit(text_sortie, textRect_Sortie)
            fenetre_sortie.blit(text_3, rec_t1) 
            fenetre_sortie.blit(text_4, rec_t2)
            # Verifier le clic de l'utilisateur
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                # Condition de sortie | Fin du Jeu
                if rec_t1.collidepoint(pos):
                    fin = True
                    arret = True
                    break
                elif rec_t2.collidepoint(pos):
                    fin = False
                    arret = False
                    go_out = True
                else:
                    fin = False
                    arret = True
                    go_out = True
        # Aucune tentation de sortie
        if(arret == False and go_out == True) : 
            final = AskChoixUser(pygame,event,display_surface,blanc,rec_1,rec_2)
            fin = final[1]
            choixUser = final[0]
            if fin == False:
                choixUser = "X" # Par default
        pygame.display.update()
        horloge.tick()

# CHECKER LE CHOIX DU USER (code ici) 
if fin == True and arret == False:
    # Création de la fenetre de Jeu
    fenetre = pygame.display.set_mode((X,Y))
    # Initialisation des variables pour le jeu
    case = initialiser_case()
    rec = init_variable(pygame, fenetre, blanc)

    is_running = True
    while is_running == True:
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
            event.key == pygame.K_q)):
                # Quitter le jeu sur QUIT [X] ou la touche "Q"
                is_running = False
                
            #redémarrage du jeu
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                # Reinitialiser les rectangles et les cases disponibles
                rec = init_variable(pygame,fenetre,blanc)
                case = initialiser_case()

            # Affichage du choix de l'Utilisateur
            texte = font_info.render('Votre choix est '+ choixUser,True,blanc,(0,0,0)) 
            # create a rectangular object for the 
            # text surface object 
            textRect = texte.get_rect()
            # copying the text surface object 
            # to the display surface object 
            fenetre.blit(texte, textRect) 

        #LOGIQUE DU JEU
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)

                # rec[0] correspond au rect_circle_switch
                # rec[1] à rec[9] correspondent aux rectangles
                if rec[1].collidepoint(pos) and case[1]:
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[35,25],[165,174], 20)
                        pygame.draw.line(fenetre, rouge,[165,25],[35,174], 20)
                        rec[0] = False
                    else:
                        # (100,100) le centre du circle, 50 rayon )        
                        pygame.draw.ellipse(fenetre, vert, [35,35,130,130], 30)
                        rec[0] = True
                    case[1] = False  
                
                if rec[2].collidepoint(pos) and case[2]:
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[210,25],[339,174], 20)
                        pygame.draw.line(fenetre, rouge,[339,25],[210,174], 20)
                        rec[0] = False
                    else:
                        # on ajoute 100 + 175 =275
                        pygame.draw.ellipse(fenetre, vert, [210,35,130,130], 30)
                        rec[0] = True
                    
                    case[2] = False
                
                if rec[3].collidepoint(pos) and case[3] :
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[385,25],[514,174], 20)
                        pygame.draw.line(fenetre, rouge,[515,25],[384,174], 20)
                        rec[0] = False
                    else:
                        pygame.draw.ellipse(fenetre, vert, [385,35,130,130], 30)
                        rec[0] = True
                    case[3] = False
                        
                if rec[4].collidepoint(pos) and case[4] :
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[35,200],[165,349], 20)
                        pygame.draw.line(fenetre, rouge,[165,200],[35,349], 20)
                        rec[0] = False
                    else:
                        pygame.draw.ellipse(fenetre, vert, [35,210,130,130], 30)
                        rec[0] = True
                    
                    case[4] = False
                    
                if rec[5].collidepoint(pos) and case[5]:
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[210,200],[339,349], 20)
                        pygame.draw.line(fenetre, rouge,[339,200],[210,349], 20)
                        rec[0] = False
                    else:
                        pygame.draw.ellipse(fenetre, vert, [210,210,130,130], 30)
                        rec[0] = True
                    
                    case[5] = False
                
                if rec[6].collidepoint(pos) and case[6]:
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[385,200],[514,349], 20)
                        pygame.draw.line(fenetre, rouge,[514,200],[384,349], 20)
                        rec[0] = False
                    else:
                        pygame.draw.ellipse(fenetre, vert, [385,210,130,130], 30)
                        rec[0] = True
                    
                    case[6] = False
                    
                if rec[7].collidepoint(pos) and case[7]:
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[35,375],[164,524], 20)
                        pygame.draw.line(fenetre, rouge,[164,375],[35,524], 20)
                        rec[0] = False
                    else:
                        pygame.draw.ellipse(fenetre, vert, [35,385,130,130], 30)
                        rec[0] = True
                    
                    case[7] = False
                
                if rec[8].collidepoint(pos) and case[8]:
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[210,375],[339,524], 20)
                        pygame.draw.line(fenetre, rouge,[339,375],[210,524], 20)
                        rec[0] = False
                    else:
                        pygame.draw.ellipse(fenetre, vert, [210,385,130,130], 30)
                        rec[0] = True
                    
                    case[8] = False
                    
                if rec[9].collidepoint(pos) and case[9]:
                    if rec[0] == True :
                        pygame.draw.line(fenetre, rouge,[385,375],[514,524], 20)
                        pygame.draw.line(fenetre, rouge,[514,375],[384,524], 20)
                        rec[0] = False
                    else:
                        pygame.draw.ellipse(fenetre, vert, [385,385,130,130], 30)
                        rec[0] = True
                    case[9] = False

        pygame.display.flip()
        #20 images par seconde, 10 moin vite que 20        
        horloge.tick(20)
    else:
        pass
elif(fin == True and arret == True):
    pygame.quit()