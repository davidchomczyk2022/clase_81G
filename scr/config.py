

width = 1100
height = 600
width_x = 300
height_y = 300
size_screen = (width,height)
origin = (0,0)
center_scree = (width // 2, height // 2)
 
center_screen_x = width // 2
center_screen_y = height // 2

FPS = 60
SPEED = 9

move_up = False
move_down = False
move_left = False
move_right = False

#----medidas de las naves ------
rect_w = 70
rect_h = 70


numero_naves = 5

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
size_button2 = (400,100)
font_color = red

def get_color(lista):
    from random import randrange
    return lista[randrange(len(lista))]
