
import pygame
from sys import exit
from config import *

#inicializar los modulos de pygame
pygame.init()


                

clock = pygame.time.Clock()

#CONFIGURO LA PANTALLA PRINCIPAL
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Primer Juego")
#---> CONFIGURO LA DIRECCION
UR = 9
DR = 3
DL = 1
UL = 7


block = pygame.Rect(300, 300, 150 ,100)
block_color = red
block_dir = UR


is_running = True
while is_running:
    clock.tick(FPS)
    #--->detectar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False

    #----> ACTUALIZO LOS ELEMNTOS------------------->
    #-->verico si el bloque choca contra los limites de la pantalla
    #--> actualizo su direccion
    if block.right >= width:
        #choco derecha
        if block_dir == DR:
            block_dir = DL
        elif block_dir == UR:
            block_dir = UL    
    elif block.left <= 0:
        #choco  izquierda
        if block_dir == UL:
            block_dir = UR
        elif block_dir == DL:
            block_dir = DR    
    elif block.top <= 0:
        # choco arriba 
        if block_dir == UL:
            block_dir = DL
        elif block_dir == UR:
            block_dir = DR    
    elif block.bottom >= height:
        # choco abajo
        if block_dir == DR:
            block_dir = UR
        elif block_dir == DL:
            block_dir = UL   
        

    #MUEVO SU BLOQUE DE ACUERDO A SU DRIRECCION
    if block_dir == DR:
        block.top += SPEED
        block.left += SPEED
    elif block_dir == DL:
        block.top += SPEED
        block.left -= SPEED
    elif block_dir == UL:
        block.top -= SPEED
        block.left -= SPEED
    elif block_dir == UR:
        block.top -= SPEED
        block.left += SPEED


    #---> dibujar pantalla-------------------->
    screen.fill(black)
    pygame.draw.rect(screen,block_color,block)

    #----->ACTUALIZO PANTALLA----------------->
    pygame.display.flip()
pygame.quit()
