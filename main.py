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

# initial est une list qui retourne 9 rectangle, switch et la variable "termine"
initial = init_variable(pygame,fenetre,blanc)
# initialisation de case vide
case = init_case()

#attention a C de Clock
horloge = pygame.time.Clock()

# initial[10] correspond à la variable "termine"
while initial[10] == False:
    #pygame.event.get() est un list
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
        event.key == pygame.K_q)):
            #true monte whie met termine = True, et attend pour 20 second 
            initial[10] = True
            
        #redémarrage du jeu
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Reinitialiser les rectangles et le switch
                initial[0:9]
                
            
    #LOGIQUE CEST ICI
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
        
            if initial[1].collidepoint(pos) and case[1]:
                if initial[0] == True :
                    pygame.draw.rect(fenetre, rouge, (50, 50, 100,100))
                    initial[0] = False
                else:
                     # (100,100) le centre du circle, 50 rayon )        
                    pygame.draw.circle(fenetre, vert, (100,100), 50)
                    initial[0] = True
                case[1] = False  
            
            if initial[2].collidepoint(pos) and case[2]:
                if initial[0] == True :
                    pygame.draw.rect(fenetre, rouge, (225, 50, 100,100))
                    initial[0] = False
                else:
                    # on ajoute 100 + 175 =275
                    pygame.draw.circle(fenetre, vert, (275,100), 50)
                    initial[0] = True
                
                case[2] = False
            
            if initial[3].collidepoint(pos) and case[3] :
                if initial[0] == True :
                    pygame.draw.rect(fenetre, rouge, (400, 50, 100,100))
                    initial[0] = False
                else:

                    pygame.draw.circle(fenetre, vert, (450,100), 50)
                    initial[0] = True
                case[3] = False
                     
            if initial[4].collidepoint(pos) and case[4] :
                if initial[0] == True :
                    pygame.draw.rect(fenetre, rouge, (50, 225, 100,100))
                    initial[0] = False
                else:
                    pygame.draw.circle(fenetre, vert, (100,275), 50)
                    initial[0] = True
                
                case[4] = False
                
            if initial[5].collidepoint(pos) and case[5]:
                if initial[0] == True :
                    pygame.draw.rect(fenetre, rouge, (225, 225, 100,100))
                    initial[0] = False
                else:
                    pygame.draw.circle(fenetre, vert, (275,275), 50)
                    initial[0] = True
                
                case[5] = False
            
            if initial[6].collidepoint(pos) and case[6]:
                if initial[0] == True :
                    pygame.draw.rect(fenetre, rouge, (400, 225, 100,100))
                    initial[0] = False
                else:
                    pygame.draw.circle(fenetre, vert, (450,275), 50)
                    initial[0] = True
                
                case[6] = False
                
            if initial[7].collidepoint(pos) and case[7]:
                if initial[0] == True :
                        pygame.draw.rect(fenetre, rouge, (50, 400, 100,100))
                        initial[0] = False
                else:
                    pygame.draw.circle(fenetre, vert, (100,450), 50)
                    initial[0] = True
                
                case[7] = False
            
            if initial[8].collidepoint(pos) and case[8]:
                if initial[0] == True :
                    pygame.draw.rect(fenetre, rouge, (225, 400, 100,100))
                    initial[0] = False
                else:
                    pygame.draw.circle(fenetre, vert, (275,450), 50)
                    initial[0] = True
                
                case[8] = False
                
            if initial[9].collidepoint(pos) and case[9]:
                if initial[0] == True :
                    pygame.draw.rect(fenetre, rouge, (400, 400, 100,100))
                    initial[0] = False
                else:
                    pygame.draw.circle(fenetre, vert,  (450,450), 50)
                    initial[0] = True
                case[9] = False
    
    #dessiner
    
       
  
 
    
    pygame.display.flip()
    
    # si on dessin le rectangle ici, on voit rien
    
    #20 images par seconde, 10 moin vite que 20        
    horloge.tick(20)
pygame.quit()