

width = 1000
height = 600
size_screen = (width,height)
origin = (0,0)
center_scree = (width // 2, height // 2)
 
center_screen_x = width // 2
center_screen_y = height // 2

FPS = 60
SPEED = 5




#COLORES
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
cyan = (0,255,255)
magenta = (255,0,255)
yelloy = (255,255,0)
custom = (255,174,201)
colors = [red,green,blue,white,cyan,magenta,yelloy,custom]

size_button = (200,50)
font_color = red

def get_color(lista):
    from random import randrange
    return lista[randrange(len(lista))]
