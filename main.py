import pygame
from Fonctional import *
pygame.init()

noir = (0, 0 ,0)
blanc = (255, 255, 255)
vert =  (0, 255, 0)
rouge = (255, 0, 0)

Taille =[600, 600]
fenetre = pygame.display.set_mode(Taille)

#Titre and Icon
pygame.display.set_caption('TIC TAC TOE')
icon = pygame.image.load('tic-tac-toe_32.png')
pygame.display.set_icon(icon)

# initial est une list qui retourne 20 élements
initial = init_variable(pygame,fenetre,blanc)

#attention a C de Clock
horloge = pygame.time.Clock()

# initial[19] correspond à la variable "termine"
while initial[19] == False:
    #pygame.event.get() est un list
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
        event.key == pygame.K_q)):
            #true monte whie met termine = True, et attend pour 20 second 
            initial[19] = True
            
        #redémarrage du jeu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Reinitialiser les rectangles ainsi que les variables de case disponible
                initial[0:18]
                
            
    #LOGIQUE CEST ICI
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
        
            if initial[0].collidepoint(pos) and initial[1]:
                if initial[18] == True :
                    pygame.draw.rect(fenetre, rouge, (50, 50, 100,100))
                    initial[18] = False
                else:
                     # (100,100) le centre du circle, 50 rayon )        
                    pygame.draw.circle(fenetre, vert, (100,100), 50)
                    initial[18] = True
                initial[1] = False  
            
            if initial[2].collidepoint(pos) and initial[3]:
                if initial[18] == True :
                    pygame.draw.rect(fenetre, rouge, (225, 50, 100,100))
                    initial[18] = False
                else:
                    # on ajoute 100 + 175 =275
                    pygame.draw.circle(fenetre, vert, (275,100), 50)
                    initial[18] = True
                
                initial[3] = False
            
            if initial[4].collidepoint(pos) and initial[5] :
                if initial[18] == True :
                    pygame.draw.rect(fenetre, rouge, (400, 50, 100,100))
                    initial[18] = False
                else:

                    pygame.draw.circle(fenetre, vert, (450,100), 50)
                    initial[18] = True
                initial[5] = False
                     
            if initial[6].collidepoint(pos) and initial[7] :
                if initial[18] == True :
                    pygame.draw.rect(fenetre, rouge, (50, 225, 100,100))
                    initial[18] = False
                else:
                    pygame.draw.circle(fenetre, vert, (100,275), 50)
                    initial[18] = True
                
                initial[7] = False
                
            if initial[8].collidepoint(pos) and initial[9]:
                if initial[18] == True :
                    pygame.draw.rect(fenetre, rouge, (225, 225, 100,100))
                    initial[18] = False
                else:
                    pygame.draw.circle(fenetre, vert, (275,275), 50)
                    initial[18] = True
                
                initial[9] = False
            
            if initial[10].collidepoint(pos) and initial[11]:
                if initial[18] == True :
                    pygame.draw.rect(fenetre, rouge, (400, 225, 100,100))
                    initial[18] = False
                else:
                    pygame.draw.circle(fenetre, vert, (450,275), 50)
                    initial[18] = True
                
                initial[11] = False
                
            if initial[12].collidepoint(pos) and initial[13]:
                if initial[18] == True :
                        pygame.draw.rect(fenetre, rouge, (50, 400, 100,100))
                        initial[18] = False
                else:
                    pygame.draw.circle(fenetre, vert, (100,450), 50)
                    initial[18] = True
                
                initial[13] = False
            
            if initial[14].collidepoint(pos) and initial[15]:
                if initial[18] == True :
                    pygame.draw.rect(fenetre, rouge, (225, 400, 100,100))
                    initial[18] = False
                else:
                    pygame.draw.circle(fenetre, vert, (275,450), 50)
                    initial[18] = True
                
                initial[15] = False
                
            if initial[16].collidepoint(pos) and initial[17]:
                if initial[18] == True :
                    pygame.draw.rect(fenetre, rouge, (400, 400, 100,100))
                    initial[18] = False
                else:
                    pygame.draw.circle(fenetre, vert,  (450,450), 50)
                    initial[18] = True
                initial[17] = False
    
    #dessiner
    
       
  
 
    
    pygame.display.flip()
    
    # si on dessin le rectangle ici, on voit rien
    
    #20 images par seconde, 10 moin vite que 20        
    horloge.tick(20)
pygame.quit()