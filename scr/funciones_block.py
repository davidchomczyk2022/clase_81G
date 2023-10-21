from aleatorios import *
from random import *
from config import *
import pygame

UR = 9
DR = 3
DL = 1
UL = 7
direcciones = (UR,DR,DL,UL)

rect_w = 30
rect_h = 30
width_coin = 20
height_coin = 20

count_coins = 20
coins = []
def create_block( left = 0,top = 0,width = 50 ,height = 50, color = (255,255,255),dir = DR,borde = 0,radio = -1):
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"dir": dir,"borde":borde,"radio":radio}

def create_conis():
    return create_block(randint(0,width - width_coin),randint(0,height - height_coin),width_coin,height_coin,yelloy,0,0,height_coin // 2)


def generate_coins(lista, count_coins):
    for i in range(count_coins):
        lista.append(create_conis())
   