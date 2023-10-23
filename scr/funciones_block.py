from aleatorios import *
from pygame.locals import *
from random import *
from config import *
import pygame
from colisiones import detectar_colision_circulo
from pygame import display, time, draw, event
from sys import exit


UR = 9
DR = 3
DL = 1
UL = 7
direcciones = (UR,DR,DL,UL)

rect_w = 40
rect_h = 40
width_coin = 20
height_coin = 20
width_coin_min = 20
height_coin_max = 30



count_coins = 5
coins = []

def terminar():
    pygame.quit()
    exit()

#-->funcion que sirve para pausar el programa    
def wait_user():
    while True:
        for evento in event.get():
            if evento.type == QUIT:
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    terminar()
                return        

def mostar_texto(superficie,texto,fuente,coordenadas,color_fuente,color_fondo):
    sup_texto = fuente.render(texto,True,color_fuente,color_fondo)
    rec_texto = sup_texto.get_rect()
    rec_texto.center = coordenadas
    superficie.blit(sup_texto,rec_texto)
    pygame.display.flip()


def create_block( imagen = None,left = 0,top = 0,width = 50 ,height = 50, color = (255,255,255),dir = DR,borde = 0,radio = -1):
    if imagen:
        imagen = pygame.transform.scale(imagen,(width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"dir": dir,"borde":borde,"radio":radio,"imagen":imagen}

def create_conis(imagen=None):
    #width_coin = randint(width_coin_min,height_coin_max)
   #height_coin = randint(width_coin_min,height_coin_max)
    return create_block(imagen,randint(0,width - width_coin),randint(0,height - height_coin),
                        width_coin,height_coin,magenta,0,0,height_coin // 2)


def generate_coins(coins, count_coins,imagen):
    for i in range(count_coins):
        coins.append(create_conis(imagen))

def dibujar_asteroide(superficie,coins):
    for coin in coins:
        if coin["imagen"]:
            superficie.blit(coin["imagen"],coin["rect"])
        else:
            pygame.draw.rect(superficie,coin["color"],coin["rect"],
                        coin["borde"],coin["radio"])
