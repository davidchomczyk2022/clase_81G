import pygame
pygame.font.init()


def mostrar_texto_centrado(screen,texto,center_x,center_y,color,fuente):
    render = fuente.render(texto,True,color)
    rect_text = render.get_rect(center = (center_x,center_y))
    #rect_text_saludar.center = rect_saludar.center
    screen.blit(render,rect_text)


def crear_boton(screen,texto,bg_color,bg_color_hover,rect_boton:pygame.Rect,font_color,fuente = pygame.font.SysFont
                (None,36)):
    if rect_boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen,bg_color_hover,rect_boton,border_radius=5) 
    else:
        pygame.draw.rect(screen,bg_color,rect_boton,border_radius=5)         
    
    mostrar_texto_centrado(screen,texto,*rect_boton.center,font_color,fuente)