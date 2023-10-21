


def calcular_radio(rect):
    return rect.height // 2

def distancia_entre_puntos(punto_1,punto_2):
    x1, y1 = punto_1
    x2, y2 = punto_2
    return  ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    



def detectar_colision_circulo(rect_1,rect_2):
    distancia = distancia_entre_puntos(rect_1.center, rect_2.center)
    return distancia <= (calcular_radio(rect_1) + calcular_radio(rect_2))

    



def detectar_colision(rect_1, rect_2):
 for r1,r2 in [(rect_1,rect_2),(rect_2,rect_1)]:
        return punto_en_rectangulo(r1.topleft,r2) or \
        punto_en_rectangulo(r1.topright, r2) or \
        punto_en_rectangulo(r1.bottomleft, r2) or \
        punto_en_rectangulo(r1.bottomright, r2)
   



    

def punto_en_rectangulo(punto, rect):
    x,y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom
