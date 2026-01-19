import pygame as pg
from figura_class import Figura
import random as ra
#Inicializar todos los módulos de pygame, patallas, objetos, eventos, sonidos, etc
pg.init()
x_pos=800
y_pos=600



#Crear pantallas o surface
pantalla = pg.display.set_mode((x_pos,y_pos)) #Definición del tamaño de pantalla en una tupla con la resolución
pg.display.set_caption("Intro Pygame") #Agrega un título en string a la ventana de juego

game_over = True
rectangulo_1= Figura(0,300,color=(201,92,56))
rectangulo_2= Figura(20,500)
rectangulo_3= Figura(0,400,color=(222,22,55))

circulo1= Figura(40,25,(123,23,26),radio=20)

lista_circulos=[]
lista_rectangulos=[]
for i in range(1,101):
    lista_circulos.append(Figura(ra.randint(0,800),ra.randint(0,600),color=(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)), radio= ra.randint(10,100)))
    lista_rectangulos.append(Figura(ra.randint(0,800),ra.randint(0,600),color=(ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)), w= ra.randint(10,100),h=ra.randint(10,100)))

while game_over:
    for eventos in pg.event.get(): #Capturar todos los eventos miéntras se ejecuta el bucle
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = False

    pantalla.fill((150, 82, 199)) #Asignar el color de pantalla en RGB

    #Recorremos la lista de circulos y rectángulos cargadas y llamamos a los metodos de mover y dibujar para que muestre en pantalla

    for i in range(0,100):
        lista_circulos[i].mover(x_pos,y_pos)
        lista_rectangulos[i].mover(x_pos,y_pos)
        lista_circulos[i].dibujar_circulo(pantalla)
        lista_rectangulos[i].dibujar_rectangulo(pantalla)



    #Agregar objetos a la pantalla
    #draw.rect(surface, color en rgb, posiciones(posicionX, posicionY, tamañoX,tamañoY)

    
    pg.display.flip() #Función para recargar todo la configuración de pantalla

#Cierre de pantalla
pg.quit() 