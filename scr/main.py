
import pygame
from aleatorios import *
from funciones_block import *
from random import *
from sys import exit
from config import *
from colisiones import detectar_colision_circulo
from pygame.locals import *



#inicializar los modulos de pygame
pygame.init()


clock = pygame.time.Clock()

#CONFIGURO LA PANTALLA PRINCIPAL
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Primer Juego")
#---> CONFIGURO LA DIRECCION
move_up = False
move_down = False
move_left = False
move_right = False


rect_w = 30
rect_h = 30
width_coin = 20
height_coin = 20
count_conis = 20

EVENT_NWE_COIN = pygame.USEREVENT + 1

pygame.time.set_timer(EVENT_NWE_COIN,3000)


block = (create_block(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h,get_color(colors),radio= 25))

coins = []
generate_coins(coins,count_coins)
cont_comer = 0


# for i in range(count_conis):
#     coins.append(create_block(randint(0,width - width_coin),randint(0,height - height_coin),width_coin,height_coin,yelloy,0,0,height_coin // 2))

#block = [pygame.Rect(300,300,150,100),red,UR]
# blocks = [,
#           {"rect":pygame.Rect(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h),"color": get_new_color(),"dir":DL,"borde":0,"radio":-1},
#           {"rect":pygame.Rect(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h),"color": get_new_color(),"dir":DR,"borde":0,"radio":-1}]


monedas = 0
fuente = pygame.font.SysFont("MV Boli",20)
texto = fuente.render(f"COINS :{monedas}",True,red)
rec_texto = texto.get_rect()
rec_texto.center = (width // 2 , 50)




is_running = True
while is_running:
    clock.tick(FPS)
    #--->detectar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            is_running = False

        if evento.type == KEYDOWN:
            if evento.key == K_RIGHT or evento.key == K_d:
                move_right = True
                move_left = False
            if evento.key == K_LEFT or evento.key == K_a:
                move_left = True
                move_right = False
            if evento.key == K_UP or evento.key == K_w:
                move_up = True
                move_down = False
            if evento.key == K_DOWN or evento.key == K_s:
                move_down = True
                move_up = False
            print(move_left,move_right,move_up,move_down)
            

        if evento.type == KEYUP:
            if evento.key == K_RIGHT:
                    move_right = False
            if evento.key == K_LEFT:
                    move_left = False
            if evento.key == K_UP:
                    move_up = False
            if evento.key == K_DOWN:
                    move_down = False
            print(move_left,move_right,move_up,move_down)
        if evento.type == EVENT_NWE_COIN:
             coins.append(create_block(randint(0,width - width_coin),randint(0,height - height_coin),
                                       width_coin,height_coin,magenta,0,0,height_coin // 2))    

        if evento.type == MOUSEBUTTONDOWN:
            new_coin = create_block(evento.pos[0],evento.pos[1],
                                       width_coin,height_coin,cyan,0,0,height_coin // 2)
            new_coin["rect"].left -= width_coin // 2
            new_coin["rect"].top -= height_coin // 2
            coins.append (new_coin)
             
    #----> ACTUALIZO LOS ELEMNTOS------------------->

 

    #MUEVO SU BLOQUE DE ACUERDO A SU DRIRECCION
   
    if move_up and block["rect"].top >= 0:
        block["rect"].top -= SPEED
    if move_down and block["rect"].bottom <= height:
        block["rect"].top += SPEED
    if move_left and block["rect"].left >= 0:
        block["rect"].left -= SPEED
    if move_right and block["rect"].right <= width:
        block["rect"].left += SPEED
   

 
    for coin in coins[:]:       
        if detectar_colision_circulo(coin["rect"],block["rect"]):
            coins.remove(coin)
            monedas += 1 
            texto = fuente.render(f"COINS :{monedas}",True,red)
            cont_comer = 20

    if len(coins) == 0:
         generate_coins(coins,count_coins)   
    if cont_comer >= 0:
        cont_comer -= 1
        block["rect"].width += 1
        block["rect"].height += 1
    else:
        block["rect"].width = rect_w
        block["rect"].height = rect_h


    #---> dibujar pantalla-------------------->
    screen.fill(black)
    screen.blit(texto,rec_texto) 

    pygame.draw.rect(screen,block["color"],block["rect"],block["borde"],block["radio"])
    for coin in coins:
          pygame.draw.rect(screen,coin["color"],coin["rect"],coin["borde"],coin["radio"])

         
    #----->ACTUALIZO PANTALLA----------------->
    pygame.display.flip()
pygame.quit()
