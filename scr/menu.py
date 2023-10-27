import pygame
from aleatorios import *
from funciones_block import *
from random import *
from sys import exit
from config import *
from colisiones import detectar_colision_circulo
from pygame.locals import *

def terminar():
    pygame.quit()
    exit()
#inicializar los modulos de pygame
pygame.init()


funte = pygame.font.SysFont()
size_button = (200,50) 
fon_color = red


#CONFIGURO LA PANTALLA PRINCIPAL
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Primer Juego")






#---> creo un reloj
clock = pygame.time.Clock()

is_running = True




while is_running:
    clock.tick(FPS)
    #--->detectar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            is_running = False
screen.fill(black)






    #----->ACTUALIZO PANTALLA----------------->
pygame.display.flip() 
terminar()
