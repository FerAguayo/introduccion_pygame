import pygame as pg
from figura_class import Rectangulo
#Inicializar todos los módulos de pygame, patallas, objetos, eventos, sonidos, etc
pg.init()
x_pos=800
y_pos=600
#Crear pantallas o sourceface
pantalla = pg.display.set_mode((x_pos,y_pos)) #Definición del tamaño de pantalla en una tupla con la resolución
pg.display.set_caption("Intro Pygame") #Agrega un título en string a la ventana de juego

game_over = True
rectangulo_1= Rectangulo(0,300,(201,92,56))
rectangulo_2= Rectangulo(20,500)
while game_over:
    for eventos in pg.event.get(): #Capturar todos los eventos miéntras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill((150, 82, 199)) #Asignar el color de pantalla en RGB

    rectangulo_1.mover(x_pos,y_pos)
    rectangulo_2.mover(x_pos,y_pos)
    #Agregar objetos a la pantalla
    #draw.rect(surface, color en rgb, posiciones(posicionX, posicionY, tamañoX,tamañoY)
    rectangulo_1.dibujar(pantalla)
    rectangulo_2.dibujar(pantalla)

    pg.display.flip() #Función para recargar todo la configuración de pantalla

#Cierre de pantalla
pg.quit() 