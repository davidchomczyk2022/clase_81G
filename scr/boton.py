from aleatorios import *
from pygame.locals import *
from random import *
from config import *
import pygame
from colisiones import detectar_colision_circulo
from pygame import display, time, draw, event
from sys import exit

#inicializar los modulos de pygame
pygame.init()

def terminar():
    pygame.quit()
    exit()
#---> creo un reloj
clock = pygame.time.Clock()

COLOR_NORMAL=(0,255,0)
COLOR_ESPECIAL = (255,0,0)
#CONFIGURO LA PANTALLA PRINCIPAL
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Primer Juego")

button_rect = pygame.Rect(300,250,200,100)

is_running = True
while is_running:
    clock.tick(FPS)
    #--->detectar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            is_running = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.post):
                color = COLOR_ESPECIAL
        elif evento.type == pygame.MOUSEBUTTONUP:
                color = COLOR_NORMAL


    pygame.draw.rect(screen,color,button_rect)

    pygame.display.flip()
terminar()
