from random import randrange



def get_color(lista):
    return lista[randrange(len(lista))]

UR = 9
DR = 3
DL = 1
UL = 7

def get_new_color():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r,g,b)

