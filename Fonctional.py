# Definition des Fonctions
import pygame

def Quitter(variableRunning):
    for event in pygame.event.get():
        if event.type == pygame.quit():
            variableRunning = False
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_q:
               variableRunning = False 