import pygame
from Fonctional import *

choixUser = "A"
while choixUser != "X" or choixUser != "O":
    print("Vous devez choisir entre X et O")
    choixUser = input("Je choisis : ")

# initialisation de pygame
pygame.init()

# Initialisation Couleur
noir = (0, 0 ,0)
blanc = (255, 255, 255)
vert =  (0, 255, 0)
rouge = (255, 0, 0)

# initialisation Screen
Taille =[600, 600]
screen = pygame.display.set_mode(Taille)

# Title and Icon
pygame.display.set_caption("TIC TAC TOE")
pygame.display.set_icon("tic-tac-toe_32.png")

# Execution Programme
is_running = True
while is_running:
    Quitter(is_running)
