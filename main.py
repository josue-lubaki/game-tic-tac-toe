import pygame
from Fonctional import *
pygame.init()

noir = (0, 0 ,0)
blanc = (255, 255, 255)
vert =  (0, 255, 0)
rouge = (255, 0, 0)

Taille =[550, 550]
fenetre = pygame.display.set_mode(Taille)

#Titre and Icon
pygame.display.set_caption('TIC TAC TOE')
icon = pygame.image.load('tic-tac-toe_32.png')
pygame.display.set_icon(icon)

# initialisation des variables rec qui corespond aux rectangles
# initialisation de case vide
case = initialiser_case()
rec = init_variable(pygame, fenetre, blanc)

#attention a C de Clock
horloge = pygame.time.Clock()
is_running = True
# is_running correspond à la variable "termine"
while is_running == True:
    #pygame.event.get() est un list
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
        event.key == pygame.K_q)):
            # Quit
            is_running = False
            
        #redémarrage du jeu
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
            # Reinitialiser les rectangles et les cases disponibles
            rec = init_variable(pygame,fenetre,blanc)
            case = initialiser_case()
                
    # LOGIQUE DU MENU DU JEU
        """ ICI """


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
    
    #dessiner

    pygame.display.flip()
    #20 images par seconde, 10 moin vite que 20        
    horloge.tick(20)
pygame.quit()