
#from  utilis import *
#from aleatorios import *
from pygame.locals import *
from random import *
from config import *
import pygame
from colisiones import detectar_colision_circulo
from pygame import display, time, draw, event
from sys import exit
pygame.font.init()

def get_color(lista):
    return lista[randrange(len(lista))]


def get_new_color():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r,g,b)
# move_right,move_left,move_up,move_left = False

UR = 9
DR = 3
DL = 1
UL = 7
direcciones = (UR,DR,DL,UL)
screen = pygame.display.set_mode(size_screen)
rect_w = 100
rect_h = 100


#--> dimenciones de las nave---
ancho_nave = 30
largo_nave = 30

ancho_nave_min = 50
largo_nave_max = 50

numero_naves = 10

speed_nave_min = 1
speed_nave_max = 2

velocidad_nave_x = 7
velocidad_nave_y = 7

velocidad_laser_y = 10
velocidad_laser_x = 7
velocidad = 7
#----------------------------------


speed_x = 7
speed_y = 7


speed_laser = 7





def get_color(lista):
    return lista[randrange(len(lista))]


def get_new_color():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r,g,b)


ESTADO_INICIO = 0
ESTADO_SALIR = 1

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
#---> funcion creo un boton y al psar x encima recreo un hover (cambio de color el boton )            
def wait_click_stark(rect_boton):
    while True:
        crear_boton(screen,"Inicio :",black,white,rect_boton,green,black)
        pygame.display.flip()
        for evento in event.get():
            if evento.type == QUIT:#al tocar la X de la ventana se cierra
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:# al tocar la tecla escape se cierra
                    terminar()
            if evento.type == MOUSEBUTTONDOWN:
                    cursor_posicion = evento.pos
                    if evento.button == 1:
                        if rect_boton.collidepoint(cursor_posicion):
                            return ESTADO_INICIO
#---------------------------------------------------------------------------------------------------------------------
def boton_salir(rect_boton):
    while True:
        crear_boton(screen,"Salir :",black,white,rect_boton,green,black)
        pygame.display.flip()
        for evento in event.get():
            if evento.type == QUIT:#al tocar la X de la ventana se cierra
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:# al tocar la tecla escape se cierra
                    terminar()
            if evento.type == MOUSEBUTTONDOWN:
                    cursor_posicion = evento.pos
                    if evento.button == 1:
                        if rect_boton.collidepoint(cursor_posicion):
                            return ESTADO_SALIR
#---------------------------------------------------------------------------------------------------------------------
def punto_en_rectangulo(punto, rect):
    x,y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom




def mostrar_texto(superficie,texto,fuente,coordenadas,color_fuente = white,color_fondo=black):
    sup_texto = fuente.render(texto,True,color_fuente,color_fondo)
    rec_texto = sup_texto.get_rect()
    rec_texto.center = coordenadas
    superficie.blit(sup_texto,rec_texto)



    

#-------------------------creo el bloque que va contener la imagenb principal
def create_block( imagen = None,left = 0,top = 0,width = 50 ,height = 50, color = (255,255,255),dir = DR,
                 borde = 0,radio = -1,speed_x = 5, speed_y = 5):
    if imagen:
        imagen = pygame.transform.scale(imagen,(width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"dir": dir,"borde":borde,"radio":radio,
            "speed_x": speed_x,"speed_y":speed_y,"imagen":imagen}

def creo_poder_laser(imagen = None,left = 0,top = 0,width = 50 ,height = 50, color = (255,255,255),speed_y = 5):
    if imagen:
        imagen = pygame.transform.scale(imagen,(width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"speed_y":speed_y,"imagen":imagen}


def naves_enemigas(imagen = None, width = 50 , height = 50):
    if imagen:
     imagen = pygame.transform.scale(imagen,(width,height))
     return{"rect":(width,height),"imagen":imagen}

#---------------------------------------------------------------------------------------------------------

def creo_naves_nuevas( imagen = None,left = 0,top = 0,width = 70 ,height = 70, color = (255,255,255),dir = DR,
                 borde = 0,radio = -1,speed_x = 10, speed_y = 7,rebote = True,bajando=True):
    if imagen:
        imagen = pygame.transform.scale(imagen,(width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"dir": dir,"borde":borde,"radio":radio,
            "speed_x":speed_x,"speed_y":speed_y,"imagen":imagen,"rebote":rebote,"bajando":bajando}


#-----------funcion se crea el laser ------------------------------------------------------------------------
def create_laser(mid_bottom=0, velocidad_laser_y = 10,color=red):
        return {"rect":pygame.Rect(mid_bottom[0] - 3,mid_bottom[1] - 8,6,16), "color":color ,"velocidad_laser_y":velocidad_laser_y}
#-------------------------------------------------------------------------------------------------------
#----> creo el laser de las naves enemigas
def create_laser_naves_enemigas(mid_bottom=0, velocidad_laser_y =7,color=Color ('red')):
        return {"rect":pygame.Rect(mid_bottom[0] - 3,mid_bottom[1] - 8,6,16),"velocidad_laser_y":velocidad_laser_y, "color":color}


#---------------------------------------------------------------------------------
#------cree la direcion de las naves de un lado a otro --------------------
def rebote_creado(block,velocidad,width):
    if block["rebote"]:
        if block["rect"].y < 100:
            block["rect"].y += velocidad
            block["rect"].x += velocidad
        if block["rect"].right <= width - 50:
            block["rect"].left += velocidad
           
        else:
            block["rebote"] = not block["rebote"]
    else:
        if block["rect"].left >= 0 + 50:
            block["rect"].left -= velocidad
          
        else:
            block["rebote"] = not block["rebote"]      
#----------------------------------------------------------------------------------------------------------------
def creo_naves(imagen = None):
    ancho_nave  = randint(ancho_nave_min,largo_nave_max)
    largo_nave = randint(ancho_nave_min,largo_nave_max)
    return creo_naves_nuevas(imagen,randint(0,width - ancho_nave),randint(-height, - largo_nave),
                        ancho_nave,largo_nave,green,0,0,largo_nave // 1,speed_y=randint(speed_nave_min,speed_nave_max))

def genero_naves(naves,numero_naves,imagen):
    for i in range(numero_naves):
        naves.append(creo_naves(imagen))
                        
#-----------------dibujo la supercie de la nave -----------------
def dibujar_naves(superficie,naves):
    for nave in naves:
        if nave["imagen"]:
            superficie.blit(nave["imagen"],nave["rect"])
        else:
            pygame.draw.rect(superficie,nave["color"],nave["rect"],
                        nave["borde"],nave["radio"])                        
#-------------------------------------------------------------

        
#----------------------dibujo la siupercie del asteroide--------------------
def dibujar_asteroide(superficie,asteroid):
    for coin in asteroid:
        if coin["imagen"]:
            superficie.blit(coin["imagen"],coin["rect"])
        else:
            pygame.draw.rect(superficie,coin["color"],coin["rect"],
                        coin["borde"],coin["radio"])
            
#-----> creo boton  y agreago la funte ala surfase--------------
def crear_boton_old(texto,size,coordenada,color,color_click,font_color):
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

def mostrar_texto_centrado(screen,texto,center_x,center_y,color,fuente):
    render = fuente.render(texto,True,color)
    rect_text = render.get_rect(center = (center_x,center_y))
    #rect_text_saludar.center = rect_saludar.center
    screen.blit(render,rect_text)

#----------------------------------------------------------------------------------------------------------------------
def crear_boton(screen,texto,bg_color,bg_color_hover,rect_boton:pygame.Rect,font_color,font_color_hover,
        fuente = pygame.font.SysFont(None,36)):
    if rect_boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen,bg_color_hover,rect_boton,border_radius=5) 
        mostrar_texto_centrado(screen,texto,*rect_boton.center,font_color_hover,fuente)
    else:
        pygame.draw.rect(screen,bg_color,rect_boton,border_radius=5)         
#------------------------------------------------------------------------------------------------------------------------------- 
    mostrar_texto_centrado(screen,texto,*rect_boton.center,font_color,fuente)
#-----------------------------------------------------------------------------------------------
def reproducir_sonido(golpe_sound):
    golpe_sound.play()
#--------------------------------------------------------------------------------------------------------------------------- 
    
#----------------------------------------------------------------------------------------------
def manejar_colision(naves, laser, score,fuente, 
                     round_two, playing_music, golpe_sound,round_three, numero_naves, imagen):
    colision  = False
    for nave in naves[:]:
        if detectar_colision_circulo(nave["rect"],laser["rect"]):
            naves.remove(nave)
            score += 1 
            texto = fuente.render(f"Score :{score}",True,red)
            rec_texto = texto.get_rect()
            rec_texto.midtop = (width // 2,30)
            #cont_comer = 10
            colision = True
            if playing_music:
                golpe_sound.play()
            if len(naves) == 0:
                genero_naves(naves,numero_naves,imagen)
                round_two.play()
            elif len(naves) == 5:
                genero_naves(naves,numero_naves,imagen)
                round_three.play()
    return colision

def manejar_rafaga(rafaga, lasers, naves, score, fuente,laser,round_three,
                     playing_music, golpe_sound, numero_naves, imagen):
    if rafaga:
        for laser in lasers[:]:
            colision = manejar_colision(naves, laser, score, fuente, playing_music, golpe_sound, numero_naves)
            if colision:
                lasers.remove(laser)
    else:
        if laser:
            colision = manejar_colision(naves,laser,score,fuente,round_three,playing_music,golpe_sound,0,numero_naves,imagen)
            if colision:
                laser = None
#------------------------------------------------------------------------------------------------
    #--->creo el movimiento del laser 
    #----> si existe el laser ?
    #-->creo la rafaga y si existe disparo la rafaga y si NO disparo norma
def laser_movimiento(laser,key:str,lasers,velo:str,rafaga):
    if rafaga:
        for laser in lasers[:]:
            if laser[key].bottom >= 0:
                laser[key].move_ip(0, -laser[velo])
            else:
                lasers.remove(laser)
    else:
        if laser:
            if laser[key].bottom >= 0:
                laser[key].move_ip(0, -laser[velo])
            else:
                laser = None
#------------------------------------------------------------------------------------------------
def mover_lasers(key:str,lasers,velo:str):
    for laser in lasers[:]:
        if laser[key].bottom >= 0:
            laser[key].move_ip(0, -laser[velo])
        else:
            lasers.remove(laser)
#---------------------------------------------------------------
trick_reverse = False
trick_slow = False

def manejar_eventos_teclado(rafaga,lasers,block,playing_music,diparo_laser,fuente,naves):
    for event in pygame.event.get():
        if event.type == QUIT:
            if event.type == pygame.KEYDOWN:
                if event.key == K_f:#-->se creo el evento del disparo laser con la letra f
                    if rafaga:#-->aca se crea la lista de laserss
                        lasers.append(create_laser(block["rect"].midtop,speed_laser,green))
                    else:
                        if not laser:#--> aca sigue normal 
                            laser = create_laser(block["rect"].midtop,speed_laser)
                        if  playing_music:
                              diparo_laser.play()
                                    
                    if event.key == K_RIGHT or event.key == K_d:
                        move_right = True
                        move_left = False

                    if event.key == K_LEFT or event.key == K_a:
                        move_left = True
                        move_right = False

                    if event.key == K_UP or event.key == K_w:
                        move_up = True
                        move_down = False

                    if event.key == K_DOWN or event.key == K_s:
                        move_down = True
                        move_up = False
    #-------------------------------------------------------------------------------

    # #-----------------> activo los efectos dados con las teclas l /r----------------------------------->
                    if event.key == K_l:
                        trick_slow = True

                    if event.key == K_r:
                        trick_reverse = True
    #-------------------------------------------------------------------------------------------------->
    #---------------> aca se utiliza la letra g para la rafaga de lasers------------------------------->
                    if event.key == K_g:
                        rafaga= True
    
    #--------------> en este evento utilizo la M del teclado para poner un pause el sonido del juego
                    if event.key == K_m:
                        if playing_music:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                        playing_music = not playing_music
    #------------->aca se pausa el juego--------------------------------------------------------------->
                    if event.key == K_p:
                        if playing_music:
                            pygame.mixer.music.pause()
                            mostrar_texto(screen,"PAUSA",fuente,center_scree,red,black)
                            wait_user()
                        if playing_music:
                            wait_user()
                            pygame.mixer.music.unpause()

            if event.type == KEYUP:
                    if event.key == K_RIGHT:
                            move_right = False
                    if event.key == K_LEFT:
                            move_left = False
                    if event.key == K_UP:
                            move_up = False
                    if event.key == K_DOWN:
                            move_down = False
                    #-->desactivo las teclas el efecto / dado
                    if event.key == K_l:
                        trick_slow = False
                    if event.key == K_r:
                        trick_reverse = False
                    #--> aca se utiliza la letra g para la rafaga de lasers(queda en FALSE)
                    if event.key == K_g:
                        rafaga = False

            for nave in naves:
                #-->movimiento normal si 
                if not trick_reverse and not trick_slow: #--> aca no pasa nada el movimiento es normal
                    if nave["rect"].top <= height:
                        nave["rect"].move_ip(0,nave["speed_y"])
                    else:
                        nave["rect"].bottom = 0
                elif trick_slow:#--> determino la velocidad mas lento con la letra l
                    if nave["rect"].top <= height:
                        nave["rect"].move_ip(0,1)
                    else:
                        nave["rect"].bottom = 0
                elif trick_reverse:#-->aca los pongo en reversa a los asteroides en caso de apretar la letra r
                    if nave["rect"].top <= height:
                        nave["rect"].move_ip(0,- nave["speed_y"])

                    return move_right,move_left,move_up,move_down,playing_music,rafaga,trick_reverse,trick_slow            


def manejar_eventos_mouse(rafaga,lasers,block,playing_music,diparo_laser):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
    #-->aca se vuelve a utilizar el laser ,con el mouse
            if event.button == 1:
                if rafaga:
                    lasers.append(create_laser(block["rect"].midtop,speed_laser,green))
                    if playing_music:
                        diparo_laser.play()
                else:    
                    if not laser:
                        laser = create_laser(block["rect"].midtop,speed_laser,red)
                    if playing_music:
                        diparo_laser.play()
            if event.button == 3:
                block["rect"].center = center_scree
            if event.type == MOUSEMOTION:
                    block["rect"].center = event.pos
                    
            #----> ACTUALIZO LOS ELEMNTOS------------------->

            # #-------------- movimientos  con las teclas de las flecha---------------------->
            
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

def manejar_eventos_juego(rafaga,DISPARO_LASER,lasers,naves,fuente,playing_music,golpe_sound,
                          laser,key:str,velocidad:str,imagen_nave2,round_two,golpe_nave,game_over_sound,block):
    for event in pygame.event.get():
        if event.type == DISPARO_LASER:
                          #--> aca recorro una copia de la lista de lasers
            if rafaga:
                for laser in lasers[:]:
                    if laser[key].bottom >= 0:
                        laser[key].move_ip(0, -laser[velocidad])
                    else:
                        #-->si el laser salio de la pantalla lo destruyo
                        lasers.remove(laser)
            else:
                if laser:
                        #--->si el laser esta dentro de la pantgalla lo muevo
                    if laser[key].bottom >= 0:
                        laser[key].move_ip(0, -laser[velocidad])
                    else:
                        #-->si el laser salio de la pantalla lo destruyo
                        laser = None
            if rafaga:
                for laser in lasers[:]:
                        #-->de detecta colicion de la nave con laser
                    colision  = False
                    for nave in naves[:]:
                        if detectar_colision_circulo(nave[key],laser[key]):
                            naves.remove(nave)
                            score += 1 
                            texto = fuente.render(f"Score :{score}",True,red)
                            rec_texto = texto.get_rect()
                            rec_texto.midtop = (width // 2,30)
                            cont_comer = 10
                            colision = True
                            if playing_music:
                                golpe_sound.play()

                            if len(naves) == 0:
                                genero_naves(naves,numero_naves,imagen_nave2)
                                round_two.play()
                            # elif len(naves) == 5:
                            #     genero_naves(naves,numero_naves,imagen_nave2)
                            #     round_three.play()
                    if colision:
                        lasers.remove(laser)
            else:
                if laser:
                        #-->de detecta colicion de la nave con el laser
                    colision  = False
                    for nave in naves[:]:
                        if detectar_colision_circulo(nave[key],laser[key]):
                            naves.remove(nave)
                            score += 1 
                            texto = fuente.render(f"Score :{score}",True,red)
                            rec_texto = texto.get_rect()
                            rec_texto.midtop = (width // 2,30)
                            cont_comer = 10
                            colision = True
                            if playing_music:
                                golpe_nave.play()
                            
                            if len(naves) == 0:
                                genero_naves(naves,numero_naves,imagen_nave2)
                                round_two.play()
                    if colision:
                        laser = None

                    #-----detecto colicion y descuento las vidas
            for nave in naves[:]:
                    if detectar_colision_circulo(nave["rect"],block["rect"]):
                        naves.remove(nave)
                        if lives > 1:
                            lives -= 1
                        else:
                            game_over_sound.play()
                            is_running = False
                        if playing_music:
                            golpe_nave.play()
                    return is_running        

def detectar_colisiones(lasers,naves,score, fuente, red, playing_music, golpe_sound, numero_naves, imagen_nave2,round_two):
    for laser in lasers[:]:
        for nave in naves[:]:
            if detectar_colision_circulo(nave["rect"], laser["rect"]):
                naves.remove(nave)
                score += 1
                texto = fuente.render(f"Score : {score}", True, red)
                rec_texto = texto.get_rect()
                rec_texto.midtop = (width // 2, 30)
                cont_comer = 10
                if playing_music:
                    golpe_sound.play()

                if len(naves) == 0:
                    genero_naves(naves, numero_naves, imagen_nave2)
                    round_two.play()

        if detectar_colision_circulo(nave["rect"], laser["rect"]):
            lasers.remove(laser)


def mover_laser(laser, rafaga, lasers):
    if rafaga:
        for laser in lasers[:]:
            if laser["rect"].bottom >= 0:
                laser["rect"].move_ip(0, -laser["velocidad_laser_y"])
            else:
                # Si el láser salió de la pantalla, se elimina
                lasers.remove(laser)
    else:
        if laser:
            # Si el láser está dentro de la pantalla, se mueve
            if laser["rect"].bottom >= 0:
                laser["rect"].move_ip(0, -laser["velocidad_laser_y"])
            else:
                # Si el láser salió de la pantalla, se elimina
                laser = None
    return laser