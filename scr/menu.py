import pygame
from aleatorios import *
from funciones_block import *
from random import *
from sys import exit
from config import *
from colisiones import detectar_colision_circulo
from pygame.locals import *
from utilis import *

pygame.font.init()

size_button = (200,50)
font_color = red

#inicializar los modulos de pygame
pygame.init()


#--> fuente
fuente = pygame.font.SysFont("comicsans",36)

#CONFIGURO LA PANTALLA PRINCIPAL
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Primer Juego")

#---> creo un reloj
clock = pygame.time.Clock()


is_running = True
rect_saludar = pygame.Rect(screen.get_width() // 2 - size_button[0] // 2, 100, *size_button)
rect_brindar = pygame.Rect(screen.get_width() // 2 - size_button[0] // 2, 160, size_button[0],size_button[1])
rect_despedir = pygame.Rect(screen.get_width() // 2 - size_button[0] // 2, 220, size_button[0],size_button[1])

while is_running:
    clock.tick(FPS)
    #--->detectar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            is_running = False  

        if evento.type == MOUSEBUTTONDOWN:
            cursor_posicion = evento.pos
            if evento.button == 1:
                if rect_saludar.collidepoint(cursor_posicion):
                    print("hola hubo click:") 
                elif rect_brindar.collidepoint(cursor_posicion):
                    print(" chin chin ...")
                elif rect_despedir.collidepoint(cursor_posicion):
                    print(" Me despiedo ::")
                    is_running = False



    screen.fill(black)



    crear_boton(screen,"Saludar", magenta,green, rect_saludar,white,black,fuente)
    crear_boton(screen,"Brindar",magenta,green,rect_brindar,black,white,fuente)
    crear_boton(screen,"Despedir",magenta,green,rect_despedir,yelloy,black,fuente)







    #--> muestro los  cambios 

    #----->ACTUALIZO PANTALLA----------------->
    pygame.display.flip() 
terminar()
