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
height_coin_max = 40

speed_x = 5
speed_y = 5

speed_coin_min = 1
speed_coin_max = 7
speed_laser = 5

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
            
def wait_click_stark(rect_boton,sup_boton):
    while True:
        for evento in event.get():
            if evento.type == QUIT:
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    terminar()
            if evento.type == MOUSEBUTTONDOWN:
                if punto_en_rectangulo(evento.pos, rect_boton):
                    sup_boton.fill(magenta)
                    #screen.blit(sup_boton,rect_boton)
                    pygame.display.flip()
            if evento.type == MOUSEBUTTONUP:
                if punto_en_rectangulo(evento.pos,rect_boton):
                    return
                         
            

def punto_en_rectangulo(punto, rect):
    x,y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom




def mostar_texto(superficie,texto,fuente,coordenadas,color_fuente = white,color_fondo=black):
    sup_texto = fuente.render(texto,True,color_fuente,color_fondo)
    rec_texto = sup_texto.get_rect()
    rec_texto.center = coordenadas
    superficie.blit(sup_texto,rec_texto)



    #pygame.display.flip() 


def create_block( imagen = None,left = 0,top = 0,width = 50 ,height = 50, color = (255,255,255),dir = DR,
                 borde = 0,radio = -1,speed_x = 5, speed_y = 5):
    if imagen:
        imagen = pygame.transform.scale(imagen,(width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"dir": dir,"borde":borde,"radio":radio,
            "speed_x": speed_x,"speed_y":speed_y,"imagen":imagen}


def create_laser(mid_bottom, speed_y = 5):

    return {"rect":pygame.Rect(mid_bottom[0] - 3,mid_bottom[1] - 8,6,16),"color":red,"speed_y":speed_y}


def create_conis(imagen=None):
    width_coin = randint(width_coin_min,height_coin_max)
    height_coin = randint(width_coin_min,height_coin_max)
    return create_block(imagen,randint(0,width - width_coin),randint(-height, - height_coin),
                        width_coin,height_coin,magenta,0,0,height_coin // 2,speed_y=randint(speed_coin_min,speed_coin_max))


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

def crear_boton(texto,size,coordenada,color,color_click,font_color):
   # fuente = pygame.font.Font(None,size[1] - 6)
    fuente = pygame.font.SysFont(None,32)
    boton = pygame.Surface(size)
    sup_texto = fuente.render(texto,True,font_color)
    rect_texto = sup_texto.get_rect()
    rect_boton = boton.get_rect()
    rect_boton.center = coordenada
    rect_texto.center = rect_boton.center
    boton.fill(color)
    boton.blit(sup_texto,rect_boton)


    return {"boton":boton,"sup_texto":sup_texto, "rect":rect_boton,"color":color,
            "color_click":color_click}



# for i in range(count_conis):
#     coins.append(create_block(randint(0,width - width_coin),randint(0,height - height_coin),width_coin,height_coin,yelloy,0,0,height_coin // 2))

#block = [pygame.Rect(300,300,150,100),red,UR]
# blocks = [,
#           {"rect":pygame.Rect(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h),"color": get_new_color(),"dir":DL,"borde":0,"radio":-1},
#           {"rect":pygame.Rect(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h),"color": get_new_color(),"dir":DR,"borde":0,"radio":-1}]
