
import pygame
from aleatorios import *
from funciones_block import *
from random import *
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
direcciones = (UR,DR,DL,UL)
rect_w = 100
rect_h = 100

count_blocks = 2


def detectar_colision(rect_1, rect_2):
    if punto_en_rectangulo(rect_1.topleft,rect_2) or \
        punto_en_rectangulo(rect_1.topright, rect_2) or \
        punto_en_rectangulo(rect_1.bottomleft, rect_2) or \
        punto_en_rectangulo(rect_1.bottomright, rect_2) or \
        punto_en_rectangulo(rect_2.topleft,rect_1) or \
        punto_en_rectangulo(rect_2.topright, rect_1) or \
        punto_en_rectangulo(rect_2.bottomleft, rect_1) or \
        punto_en_rectangulo(rect_2.bottomright, rect_1):
            return True
    else:
        return False



    

def punto_en_rectangulo(punto, rect):
    x,y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom




blocks = []

for block in range(count_blocks):
    blocks.append(create_block(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h,get_color(colors),choice(direcciones)))



#block = [pygame.Rect(300,300,150,100),red,UR]
# blocks = [,
#           {"rect":pygame.Rect(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h),"color": get_new_color(),"dir":DL,"borde":0,"radio":-1},
#           {"rect":pygame.Rect(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h),"color": get_new_color(),"dir":DR,"borde":0,"radio":-1}]
     

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
    for block in blocks:
        if block["rect"].right >= width:
            #choco derecha
            if block["dir"] == DR:
                block["dir"] = DL
            elif block["dir"] == UR:
                block["dir"]= UL 
            block["color"] = get_new_color()      
        elif block["rect"].left <= 0:
                #choco  izquierda
                if block["dir"] == UL:
                    block["dir"] = UR
                elif block["dir"] == DL:
                    block["dir"] = DR    
                block["borde"] = randrange(31)    
        elif block["rect"].top <= 0:
                # choco arriba 
                if block["dir"] == UL:
                    block["dir"] = DL
                elif block["dir"] == UR:
                 block["dir"] = DR    
        elif block["rect"].bottom >= height:
                # choco abajo
                if block["dir"] == DR:
                    block["dir"] = UR
                elif block["dir"]== DL:
                    block["dir"] = UL   
                block["radio"] = randint(-1, 25)

    #MUEVO SU BLOQUE DE ACUERDO A SU DRIRECCION
    for block in blocks:
        if block["dir"] == DR:
            block["rect"].top += SPEED
            block["rect"].left += SPEED
        elif block["dir"] == DL:
            block["rect"].top += SPEED
            block["rect"].left -= SPEED
        elif block["dir"] == UL:
            block["rect"].top -= SPEED
            block["rect"].left -= SPEED
        elif block["dir"] == UR:
            block["rect"].top -= SPEED
            block["rect"].left += SPEED
    if detectar_colision(blocks[0]["rect"],blocks[1]["rect"]):
        print("COLISION!!!!!!!")

    #---> dibujar pantalla-------------------->
    screen.fill(black)
    for block in blocks:
        pygame.draw.rect(screen,block["color"],block["rect"],block["borde"],block["radio"])

    #----->ACTUALIZO PANTALLA----------------->
    pygame.display.flip()
pygame.quit()
