
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


UR = 9
DR = 3
DL = 1
UL = 7
direcciones = (UR,DR,DL,UL)
screen = pygame.display.set_mode(size_screen)
rect_w = 40
rect_h = 40
width_coin = 20
height_coin = 20

#--> dimenciones de las nave---
ancho_nave = 20
largo_nave = 20

ancho_nave_min = 50
largo_nave_max = 50

numero_naves = 5
speed_nave_min = 1
speed_nave_max = 4
#----------------------------------


speed_x = 7
speed_y = 7


speed_laser = 5

count_asteroid = 5



def get_color(lista):
    return lista[randrange(len(lista))]


def get_new_color():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r,g,b)




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
        crear_boton(screen,"Comenzar",red,white,rect_boton,cyan,black)
        pygame.display.flip()
        for evento in event.get():
            if evento.type == QUIT:
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    terminar()
            if evento.type == MOUSEBUTTONDOWN:
                    cursor_posicion = evento.pos
                    if evento.button == 1:
                        if rect_boton.collidepoint(cursor_posicion):
                            return None

def punto_en_rectangulo(punto, rect):
    x,y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom




def mostrar_texto(superficie,texto,fuente,coordenadas,color_fuente = white,color_fondo=black):
    sup_texto = fuente.render(texto,True,color_fuente,color_fondo)
    rec_texto = sup_texto.get_rect()
    rec_texto.center = coordenadas
    superficie.blit(sup_texto,rec_texto)



    #pygame.display.flip() 

#-------------------------creo el bloque que va contener la imagenb principal
def create_block( imagen = None,left = 0,top = 0,width = 50 ,height = 50, color = (255,255,255),dir = DR,
                 borde = 0,radio = -1,speed_x = 5, speed_y = 5):
    if imagen:
        imagen = pygame.transform.scale(imagen,(width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"dir": dir,"borde":borde,"radio":radio,
            "speed_x": speed_x,"speed_y":speed_y,"imagen":imagen}


#----------------------------------------------------------------------------------

def creo_naves_nuevas( imagen = None,left = 0,top = 0,width = 70 ,height = 70, color = (255,255,255),dir = DR,
                 borde = 0,radio = -1,speed_x = 5, speed_y = 5):
    if imagen:
        imagen = pygame.transform.scale(imagen,(width,height))
    return {"rect":pygame.Rect(left,top,width,height),"color":color,"dir": dir,"borde":borde,"radio":radio,
            "speed_x": speed_x,"speed_y":speed_y,"imagen":imagen}


#-----------funcion se crea el laser ------------------------------------------------------------
def create_laser(mid_bottom=0, speed_y = 5,color=red):
        return {"rect":pygame.Rect(mid_bottom[0] - 3,mid_bottom[1] - 8,6,16), "color":color ,"speed_y":speed_y}


# def create_conis(imagen=None):
#     width_coin = randint(width_coin_min,height_coin_max)
#     height_coin = randint(width_coin_min,height_coin_max)
#     return create_block(imagen,randint(0,width - width_coin),randint(-height, - height_coin),
#                         width_coin,height_coin,magenta,0,0,height_coin // 2,speed_y=randint(speed_coin_min,speed_coin_max))
#---------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
def creo_naves(imagen = None):
    ancho_nave  = randint(ancho_nave_min,largo_nave_max)
    largo_nave = randint(ancho_nave_min,largo_nave_max)
    return creo_naves_nuevas(imagen,randint(0,width - ancho_nave),randint(-height, - largo_nave),
                        ancho_nave,largo_nave,green,0,0,largo_nave // 2,speed_y=randint(speed_nave_min,speed_nave_max))

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
#---------------creo nuevos asteroides--------------------------------------
# def generate_asteroid(asteroid, count_asteroid,imagen):
#     for i in range(count_asteroid):
#         asteroid.append(create_conis(imagen))
        
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


def crear_boton(screen,texto,bg_color,bg_color_hover,rect_boton:pygame.Rect,font_color,font_color_hover,
        fuente = pygame.font.SysFont(None,36)):
    if rect_boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen,bg_color_hover,rect_boton,border_radius=5) 
        mostrar_texto_centrado(screen,texto,*rect_boton.center,font_color_hover,fuente)
    else:
        pygame.draw.rect(screen,bg_color,rect_boton,border_radius=5)         
    
    mostrar_texto_centrado(screen,texto,*rect_boton.center,font_color,fuente)

# for i in range(count_conis):
#     coins.append(create_block(randint(0,width - width_coin),randint(0,height - height_coin),width_coin,height_coin,yelloy,0,0,height_coin // 2))

#block = [pygame.Rect(300,300,150,100),red,UR]
# blocks = [,
#           {"rect":pygame.Rect(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h),"color": get_new_color(),"dir":DL,"borde":0,"radio":-1},
#           {"rect":pygame.Rect(randint(0,width - rect_w),randint(0,height - rect_h),rect_w,rect_h),"color": get_new_color(),"dir":DR,"borde":0,"radio":-1}]

    # pygame.draw.rect(screen,magenta,rect_saludar,border_radius=5)
    # render_saludar = fuente.render("saludar",True,font_color)
    # rect_text_saludar = render_saludar.get_rect(center = rect_saludar.center )
    # #rect_text_saludar.center = rect_saludar.center
    # screen.blit(render_saludar,rect_text_saludar)

    
    # pygame.draw.rect(screen,magenta,rect_brindar,border_radius=5)
    # render_brindar = fuente.render("brindar",True,font_color)
    # rect_text_brindar = render_brindar.get_rect(center = rect_brindar.center )
    # #rect_text_saludar.center = rect_saludar.center
    # screen.blit(render_brindar,rect_text_brindar)


    # pygame.draw.rect(screen,magenta,rect_despedir,border_radius=5)
    # render_despedir = fuente.render("despedir",True,font_color)
    # rect_text_despedir = render_despedir.get_rect(center = rect_despedir.center )
    # #rect_text_saludar.center = rect_saludar.center
    # screen.blit(render_despedir,rect_text_despedir)