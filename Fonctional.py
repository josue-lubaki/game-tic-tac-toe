# Reinitialisation des Rectangles
def init_variable(pygame, screen, color):
    # on ajout 175 à x donc on commence par 25, 25+175 = 200, 200+175=  375
    r1 = pygame.draw.rect(screen, color, (25,25,150,150))
    # (255,255,255) coleur color, on change x a 200 
    r2 = pygame.draw.rect(screen, (255,255,255), (200,25,150,150))
    r3 = pygame.draw.rect(screen, color, (375,25,150,150))
    #y starts at 200
    r4 = pygame.draw.rect(screen, color, (25,200,150,150))
    r5 = pygame.draw.rect(screen, color, (200,200,150,150))
    r6 = pygame.draw.rect(screen, color, (375,200,150,150))
    #y starts at 375
    r7 = pygame.draw.rect(screen, color, (25,375,150,150))
    r8 = pygame.draw.rect(screen, color, (200,375,150,150))
    r9 = pygame.draw.rect(screen, color, (375,375,150,150))

    #boucle jusqu'à ce que l'utilisateur décide de fermer la fenêtre
    rect_circle_switch = True
    return [rect_circle_switch,r1,r2,r3,r4,r5,r6,r7,r8,r9]

# Reinitialisation des cases disponibles
def initialiser_case():
    c1 = True
    c2 = True
    c3 = True
    c4 = True
    c5 = True
    c6 = True
    c7 = True
    c8 = True
    c9 = True
    return [False,c1,c2,c3,c4,c5,c6,c7,c8,c9]

# Definition des Fonts Utilisés pour les textes
def FontUse(pygame):
    font_titre = pygame.font.Font('freesansbold.ttf', 38)
    font = pygame.font.Font('freesansbold.ttf', 32) 
    font_info = pygame.font.Font('freesansbold.ttf', 24)
    return [font_titre,font,font_info]

# Definition de la Taille de la fenetre
def DimensionFenetre():
    X = 550
    Y = 550
    return [X,Y]

# Les diffrentes Couleurs Utilisés pour les Fonctions
blue = (0, 0, 128) 
noir = (0, 0 ,0)
blanc = (255, 255, 255)
vert =  (0, 255, 0)
rouge = (255, 0, 0)
rouge_sombre = (153,0,0) 
blue_sombre = (0,51,51)
orange_sombre = (204,102,0)
orange_claire = (255,128,0)

# Fonction demandant à l'Utilisateur de choisir son symbole (X|O)
def AskChoixUser(pygame,event,fenetre,rec_1,rec_2):
    fin = False
    result = "X"
    if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        print(pos)
        if rec_1.collidepoint(pos):
            choixUser = "X"
        elif rec_2.collidepoint(pos):
            choixUser = "O"
        else:
            choixUser = "X [default]"
        # Deplacer les cases de choix vers l'origine (0,0)
        if choixUser == "X" or choixUser == "O":
            rec_1 = pygame.draw.rect(fenetre, blanc, (0,0,0,0))
            rec_2 = pygame.draw.rect(fenetre, blanc, (0,0,0,0))
            if choixUser == "X" :
                result = choixUser # X
                fin = True
            else:
                result = choixUser # O
                fin = True
        else:
            fin = False
    return [result,fin]


def ConfirmationQuitter(pygame,fenetre_sortie):
    # Dimension fenetre
    dimension = DimensionFenetre()
    X = dimension[0]
    Y = dimension[1]
    display_surface = pygame.display.set_mode((X, Y ))
    # Font Utilisé
    font_Utilise = FontUse(pygame)
    font_titre = font_Utilise[0]
    font =  font_Utilise[1]  
      
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
                    print(pos, " - ConfirmationQuitter()")
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
                final = AskChoixUser(pygame,event,display_surface,rec_1,rec_2)
                fin = final[1]
                choixUser = final[0]
                if fin == False:
                    choixUser = "X" # Par default
            pygame.display.update()
            horloge.tick()
    return [choixUser,fin,arret]