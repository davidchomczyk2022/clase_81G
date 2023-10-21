
import pygame
from sys import exit
from config import *

#inicializar los modulos de pygame
pygame.init()
clock = pygame.time.Clock()

#CONFIGURO LA PANTALLA PRINCIPAL
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Primer Juego")




#fuente = pygame.font.Font(None,36)
fuente = pygame.font.SysFont("MV Boli",48)

contador = 0


is_running = True
while is_running:
    clock.tick(FPS)
    #--->detectar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False
    contador += 1
    #----> ACTUALIZO LOS ELEMNTOS------------------->
    texto = fuente.render(f"Contador :{contador}",True,red)
    rec_texto = texto.get_rect()
    rec_texto.center = center_scree

    
    
    #---> dibujar pantalla-------------------->
    screen.fill(black)
    screen.blit(texto,rec_texto)


    #----->ACTUALIZO PANTALLA----------------->
    pygame.display.flip()
pygame.quit()
