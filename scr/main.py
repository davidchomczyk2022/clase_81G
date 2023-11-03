
import pygame
#from aleatorios import *
from funciones_block import *
from random import randint, randrange
from sys import exit
from config import *
from colisiones import detectar_colision_circulo
from pygame.locals import *
#from utilis import *




#inicializar los modulos de pygame
pygame.init()

#---> creo un reloj
clock = pygame.time.Clock()

#CONFIGURO LA PANTALLA PRINCIPAL
screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Primer Juego")

#---> CONFIGURO LA DIRECCION

move_up = False
move_down = False
move_left = False
move_right = False


rect_w = 70
rect_h = 70
width_coin = 30
height_coin = 30

count_conis = 20

#--->seteo sonidos 
golpe_sound = pygame.mixer.Sound("./scr/sonidos/ungolpe_prev.mp3")
round_two = pygame.mixer.Sound("./scr/sonidos/round-two.mp3")
round_three = pygame.mixer.Sound("./scr/sonidos/round-three.mp3")
game_over_sound = pygame.mixer.Sound("./scr/sonidos/game-over-1-gameover.mp3")
background = pygame.transform.scale(pygame.image.load("./scr/sonidos/espacio_01.jpg"),size_screen)
#--->musica  fondo (solo 1 se permite)
pygame.mixer.music.load("./scr/sonidos/stranger-things-124008.mp3")


# --->  sonido .PLAY tiene 3 parametros
#pygame.mixer.music.play()

#-->control de volumen 
pygame.mixer.music.set_volume(0.2)
playing_music = True

#-->creo boton

btn_comenzar= pygame.Rect(screen.get_width() // 2 - size_button[0] // 2, 100, *size_button)
#--->CARGA DE IMAGENES

imagen_player = pygame.image.load("./scr/sonidos/nave_01.webp")
imagen_asteroide = pygame.image.load("./scr/sonidos/asteroide_2.jpg")

#-->eventos personales
EVENT_NWE_COIN = pygame.USEREVENT + 1

pygame.time.set_timer(EVENT_NWE_COIN,3000)


block = create_block(imagen_player,randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h,get_color(colors),radio= 30)
max_contador = 0

while True:#--> aca se reinicia el juego en un bucle
    #---> aca en este punto se reinicia el juego , en un bucle el
    #--> score empieza desde cero
    #---> extablesco fuente
    laser = None
    monedas = 0
    rafaga = False
    lives = 3

    fuente = pygame.font.SysFont("MV Boli",20)
    texto = fuente.render(f"COINS :{monedas}",True,red)
    rec_texto = texto.get_rect()
    rec_texto.midtop = (width // 2 , 30)

    mostrar_texto(screen,f"Lives: {lives}",fuente,(200, height -50),magenta)
    
    #---> creo lista de coins
    coins = []
    generate_coins(coins,count_coins,imagen_asteroide)
    cont_comer = 0

    #-->creo una lista de laseres
    lasers = []


    #--> aca lo vuelvo hacer vicible al cursos del mouse
    pygame.mouse.set_visible(True)

    screen.fill(black)
    mostrar_texto(screen,"Asteroides",fuente,(width //2 ,50 ),green)
   #-->creo el boron,, lo muestro en su estado final
   
    pygame.display.flip()
    wait_click_stark(btn_comenzar)

    #---> aca dejo invicible el mouse
    pygame.mouse.set_visible(False)

    pygame.mixer.music.play(-1)

    trick_reverse = False
    trick_slow = False
    

    is_running = True

    while is_running:

        clock.tick(FPS)
        #--->detectar los eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                is_running = False

            if evento.type == KEYDOWN:
                #-->se creo el evento del disparo laser con la letra f
                if evento.key == K_f:
                    if rafaga:#-->aca se crea la lista de laserssssss
                        lasers.append(create_laser(block["rect"].midtop,speed_laser,green))
                    else:
                        if not laser:#--> aca sigue normal 
                            laser = create_laser(block["rect"].midtop,speed_laser)
                #---> se recrea los movimientos con las teclas d / a / w / s
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
                #--> activo los efectos dados con las teclas l /r
                if evento.key == K_l:
                    trick_slow = True

                if evento.key == K_r:
                    trick_reverse = True
                #--> aca se utiliza la letra g para la rafaga de lasers
                if evento.key == K_g:
                    rafaga= True
                #----> en este evento utilizo la M del teclado para poner un pause el sonido del juego
                if evento.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music
                #------>aca se pausa el juego
                if evento.key == K_p:
                    if playing_music:
                        pygame.mixer.music.pause()
                        mostrar_texto(screen,"PAUSA",fuente,center_scree,red,black)
                        wait_user()
                    if playing_music:
                        wait_user()
                        pygame.mixer.music.unpause()
                    


            # print(move_left,move_right,move_up,move_down)
            if evento.type == KEYUP:
                if evento.key == K_RIGHT:
                        move_right = False
                if evento.key == K_LEFT:
                        move_left = False
                if evento.key == K_UP:
                        move_up = False
                if evento.key == K_DOWN:
                        move_down = False
                #-->desactivo las teclas el efecto / dado
                if evento.key == K_l:
                    trick_slow = False
                if evento.key == K_r:
                    trick_reverse = False
                 #--> aca se utiliza la letra g para la rafaga de lasers(queda en FALSE)
                if evento.key == K_g:
                    rafaga = False
                #print(move_left,move_right,move_up,move_down)
            if evento.type == EVENT_NWE_COIN:
                coins.append(create_block(imagen_asteroide,randint(0,width - width_coin),randint(0,height - height_coin),
                                        width_coin,height_coin,green,0,0,height_coin // 2))    

            if evento.type == MOUSEBUTTONDOWN:
                #-->aca se vuelve a utilizar el laser ,con el mouse
                if evento.button == 1:
                    if rafaga:
                        lasers.append(create_laser(block["rect"].midtop,speed_laser,green))
                    else:    
                        if not laser:
                            laser = create_laser(block["rect"].midtop,speed_laser)
                        # new_coin = create_block(imagen_asteroide,evento.pos[0],evento.pos[1],
                        # width_coin,height_coin,cyan,0,0,height_coin // 2)
                        # new_coin["rect"].left -= width_coin // 2
                        # new_coin["rect"].top -= height_coin // 2
                        # coins.append (new_coin)
                if evento.button == 3:
                    block["rect"].center = center_scree
    #----> aca es cuando el mouse se mueva por l apantalla del juego
            if evento.type == MOUSEMOTION:
                block["rect"].center = evento.pos
                
        #----> ACTUALIZO LOS ELEMNTOS------------------->

    

        #MUEVO SU BLOQUE DE ACUERDO A SU DRIRECCION
    
        if move_up and block["rect"].top >= 0:
            #-->muevo arriba
            block["rect"].top -= SPEED
        if move_down and block["rect"].bottom <= height:
            #--> muevo abajo
            block["rect"].top += SPEED
        if move_left and block["rect"].left >= 0:
            #--->muevo izquierda
            block["rect"].left -= SPEED
        if move_right and block["rect"].right <= width:
            #-->muevo derecha
            block["rect"].left += SPEED


        pygame.mouse.set_pos(block["rect"].centerx,block["rect"].centery)
    

        #--->muevo los asteroides en caida
        for coin in coins:
            #-->movimiento normal si 
            if not trick_reverse and not trick_slow: #--> aca no pasa nada el movimiento es normal
                if coin["rect"].top <= height:
                    coin["rect"].move_ip(0,coin["speed_y"])
                else:
                    coin["rect"].bottom = 0
            elif trick_slow:#--> determino la velocidad mas lento con la letra l
                if coin["rect"].top <= height:
                    coin["rect"].move_ip(0,1)
                else:
                    coin["rect"].bottom = 0
            elif trick_reverse:#-->aca los pongo en reversa a los asteroides en caso de apretar la letra r
                if coin["rect"].top <= height:
                    coin["rect"].move_ip(0,- coin["speed_y"])
    
            #--->creo el movimiento del laser 
            #----> si existe el laser ?
    #-->creo la rafaga y si existe disparo la rafaga y si NO disparo normal
        if rafaga:#--> aca recorro una copia de la lista de lasers
            for laser in lasers[:]:
                if laser["rect"].bottom >= 0:
                    laser["rect"].move_ip(0, -laser["speed_y"])
                else:
                    #-->si el laser salio de la pantalla lo destruyo
                    lasers.remove(laser)
        else:
            if laser:
                    #--->si el laser esta dentro de la pantgalla lo muevo
                if laser["rect"].bottom >= 0:
                    laser["rect"].move_ip(0, -laser["speed_y"])
                else:
                    #-->si el laser salio de la pantalla lo destruyo
                    laser = None
        if rafaga:
            for laser in lasers[:]:
                    #-->de detecta colocion de la nave con asteroides
                colision  = False
                for coin in coins[:]:
                    if detectar_colision_circulo(coin["rect"],laser["rect"]):
                        coins.remove(coin)
                        monedas += 1 
                        texto = fuente.render(f"COINS :{monedas}",True,red)
                        rec_texto = texto.get_rect()
                        rec_texto.midtop = (width // 2,30)
                        cont_comer = 10
                        colision = True
                        if playing_music:
                            golpe_sound.play()
                        
                        if len(coins) == 0:
                            generate_coins(coins,count_coins,imagen_asteroide)
                            round_two.play()
                        elif len(coin) == 0:
                            round_three.play()
                if colision:
                    lasers.remove(laser)
        else:
            if laser:
                    #-->de detecta colocion de la nave con asteroides
                colision  = False
                for coin in coins[:]:       
                    if detectar_colision_circulo(coin["rect"],laser["rect"]):
                        coins.remove(coin)
                        monedas += 1 
                        texto = fuente.render(f"COINS :{monedas}",True,red)
                        rec_texto = texto.get_rect()
                        rec_texto.midtop = (width // 2,30)
                        cont_comer = 10
                        colision = True
                        if playing_music:
                            golpe_sound.play()
                        
                        if len(coins) == 0:
                            generate_coins(coins,count_coins,imagen_asteroide)
                            round_two.play()
                        elif len(coin) == 0:
                            round_three.play()
                if colision:
                    laser = None

        for coin in coins[:]:       
                if detectar_colision_circulo(coin["rect"],block["rect"]):
                    coins.remove(coin)
                    if lives > 1:
                        lives -= 1
                    else:
                        game_over_sound.play()
                        is_running = False
                        cont_comer = 10
                    if playing_music:
                        golpe_sound.play()
                
                if len(coins) == 0:
                    generate_coins(coins,count_coins,imagen_asteroide)
                    round_two.play()
                elif len(coin) == 0:
                    round_three.play()
            
        if cont_comer >= 0:
            cont_comer -= 1
            block["rect"].width = rect_w + 5
            block["rect"].height = rect_h + 5
        else:
            block["rect"].width = rect_w
            block["rect"].height = rect_h


        #---> dibujar pantalla-------------------->
        #screen.fill(black)
        screen.blit(background,origin)

        dibujar_asteroide(screen,coins)
            

        #pygame.draw.rect(screen,block["color"],block["rect"],block["borde"],block["radio"])
        screen.blit(block["imagen"],block["rect"])
        #-->creo el lasery creo la rafaga de lasers
        if rafaga:
            for laser in lasers:
                pygame.draw.rect(screen,laser["color"],laser["rect"])
        else:
            if laser:
                pygame.draw.rect(screen,laser["color"],laser["rect"])
        

        screen.blit(texto,rec_texto) 
        #---> aca mostramos las vidas que tenemos al comenzar
        mostrar_texto(screen,f"Lives: {lives}",fuente,(200, height -50),magenta)
       
        #----->ACTUALIZO PANTALLA----------------->
        pygame.display.flip()


    if monedas > max_contador:
        max_contador = monedas

    #--> aca doy los mensajes del score el juego termino y una tecla precionar para continuar
    pygame.mixer.music.stop()
    game_over_sound.play()
    screen.fill(black)
    mostrar_texto(screen,f"Score:{monedas}",fuente,(140, 20),green)
    mostrar_texto(screen,f"Top Score:{max_contador}",fuente,(width - 150, 20),green)
    mostrar_texto(screen,"Game Over",fuente,center_scree,red)
    mostrar_texto(screen,"Presione una tecla para comenzar....",fuente,(width //2 , height - 50 ),blue)
    pygame.display.flip()
    wait_user()

terminar()

