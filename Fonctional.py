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
