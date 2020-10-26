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

def AskChoixUser(pygame,event,fenetre,color,rec_1,rec_2):
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
            rec_1 = pygame.draw.rect(fenetre, color, (0,0,0,0))
            rec_2 = pygame.draw.rect(fenetre, color, (0,0,0,0))
            if choixUser == "X" :
                result = choixUser # X
                fin = True
            else:
                result = choixUser # O
                fin = True
        else:
            fin = False
    return [result,fin]

def ConfirmationDepart(pygame,event,fenetre_sortie,font,font_titre,X,Y,vert,noir,blanc,rouge_sombre,orange_sombre,blue_sombre):
            pygame.display.update()
            fenetre_sortie = pygame.display.set_mode((X,Y)) # definition fenetre
            # Coder ici | User veut partir | text de confirmation
            fenetre_sortie.fill(blue_sombre) # color fond
            fin = False
            arret =False
            go_out =False
            # TEXT
            text_sortie = font.render('Voulez-vous Quitter la Partie ?', True, orange_sombre)
            text_3 = font_titre.render('OUI', True, vert, noir)
            text_4 = font_titre.render('NON', True, rouge_sombre,noir)
            # Allouer l'espace necessaire pour le text
            textRect_Sortie = text_sortie.get_rect() 
            rec_t1 = pygame.draw.rect(fenetre_sortie, blanc, (150,250,100,80))
            rec_t2 = pygame.draw.rect(fenetre_sortie, blanc, (300,250,100,80))
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
                if rec_t1.collidepoint(pos):
                    fin = True
                    arret = True
                elif rec_t2.collidepoint(pos):
                    fin = False
                    arret = False
                    go_out = True
                else:
                    fin = False
                    arret = True
            return [rec_t1,rec_t2,arret,go_out,fin]