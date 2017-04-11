#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rama principal


# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame, pygame.event
from pygame.locals import *
import sys
import time
import main2
import listennerMando
import TelegramBot

DatosIniciales=main2.PrimerasIncidencias()
#DatosIniciales=0

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640

SCREEN_HEIGHT = 480

Incidencias=["Cocina rota", "Baño roto", "Mando de televisión sin pilas", "Suelo roto", "Robaron Jabones", "Robaron dvd", "Se acabo el gas", "No tengo electricidad","Cocina rota1", "Baño roto1", "Mando de televisión sin pilas1", "Suelo roto1", "Robaron Jabones1", "Robaron dvd1", "Se acabo el gas1", "No tengo electricidad1"]


# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------

def get_key():
    
    while 1:
        event = pygame.event.poll()
        # print event # para ver los eventos posibles
        #time.sleep(1)
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def get_Mando_key():
    
    while 1:
        eventMado = listennerMando.infoMando()
        print "entrada de mando solicitada, se devuelve . ", eventMado
        # print event # para ver los eventos posibles
        #time.sleep(1)
        if eventMado!=[]:
            return eventMado
        else:
            pass

class Text:
    def __init__(self, FontName = None, FontSize = 30):
        pygame.font.init()
        self.font = pygame.font.Font(FontName, FontSize)
        self.size = FontSize
 
    def render(self, surface, text, color, pos):
        text = unicode(text, "UTF-8")
        x, y = pos
        for i in text.split("\r"):
            surface.blit(self.font.render(i, 1, color), (x, y))
            y += self.size   

# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos las proporciones

    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    modes = pygame.display.list_modes(0)

    #Adaptado a pantalla
    #screen = pygame.display.set_mode(modes[0])

    #Fullscreen
    screen = pygame.display.set_mode(modes[0], FULLSCREEN)

    # creamos la ventana y le indicamos un titulo:
    pygame.display.set_caption("Demola Tecina")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    #fondo = pygame.image.load("fondo.jpg").convert()
    tux = pygame.image.load("tux.png").convert_alpha()

    tux_pos_x = 640/2
    tux_pos_y = 200


    # Bucle principal del programa

    Ejey=0
    eleccion=0
    Bandera=False
    inkey=0
    UsamosMando=False
    ContCrash = 0
    
    while True:
        

        #time.sleep(1)
        color = (0, 0, 0)
        screen.fill(color)


        Cont=0


        # Aqui buscamos el alto de la pantalla y repartimos las incidencias entre 
        #el alto de la pantalla para repartirlas unifomemente

        Pantalla = (screen.get_height()/len(Incidencias))

        #Generacion de posibles

        Posibles=[]
        Cont2=0
        for Incidencia in Incidencias:
            
            Pantalla1=Pantalla*Cont2
            Posibles.insert(Cont2,Pantalla1)
            Cont2=Cont2+1
            
        #Posibles=[0, 130, 260, 390, 520, 650, 780]

        text = Text()
        ContInv = len(Posibles)
        for Incidencia in Incidencias:
            #print Incidencia

            
            if eleccion<0:
                eleccion=len(Incidencias)-1

            if eleccion>len(Incidencias)-1:
                eleccion=0

            #Para debugging, aqui dejo el numero de tiene seleccionado la persona
            #print eleccion

            Cont=Posibles[ContInv-1]
            ContInv=ContInv-1


            
            #Genero un corrector porque el cuadro de seleccion me da problemas

            Corrector=(screen.get_height()/10.80)-20 #El corrector parece funcionar bien para longitudes de lista pequeñas, para grandes, hace falta aplicar un corrector grande

            #Posicion que ocupa el rectangulo blanco en la pantalla
            Ejex=(screen.get_width() / 2) - 102
            Ejey=(screen.get_height()-Posibles[eleccion]-Corrector )

            pygame.draw.rect(screen, (255,255,255), ( Ejex, Ejey , 500,60), 1)  #1= Ancho de linea. Modifica hacia abajo, hacia arriba, derecha 
                        

            #Posicion que ocupan las incidencias en la pantalla
            Ejex=(screen.get_width() / 2) - 100
            Ejey=(Cont+20)

            text.render(screen, Incidencia, (255, 255, 255), (Ejex,  Ejey) ) #Dibujamos el Texto
            #time.sleep(1)
            
        
  



        #Controles para cerrar el programa por botones

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                exit()
       

        # Renderizado de objetos

        screen.blit(tux, (tux_pos_x, tux_pos_y))

        # se muestran lo cambios en pantalla
        pygame.display.flip()








        # Activamos el reconocimeinto del teclado
        # Aqui probamos si esta activo el modulo ListennerMando.py, si lo está, lo ejecuta, si no esta, busca el teclado
        
       #Se genera una variable para controlar cuando se utliza mando a distancia y cuando no, para no llamar a modulos que no existen en desarrollo

        UsamosMando = False
        
        if UsamosMando == True:
            inkey = get_Mando_key()
            print inkey    
            UsamosMando = True
            
            Teclas = {"KEY_0":256, "KEY_1":257, "KEY_2":258, "KEY_3":259, "KEY_4":260, "KEY_5":261, "KEY_6":262, "KEY_7":263, "KEY_8":264, "KEY_9":265, "KEY_UP":273, "KEY_LEFT":276, "KEY_RIGHT":275,"KEY_DOWN":274, "KEY_ENTER":13}
            inkey = Teclas[inkey]
        else:
            
            inkey = get_key()





        # Controles de teclado

        if inkey >= 256 and inkey < 266:#Operativizamos el pad numerico
            dic={256:0,257:1,258:2,259:3,260:4,261:5,262:6,263:7,264:8,265:9}
            eleccion = dic[inkey]


        #Crasheo por mando a distancia
        if UsamosMando == True and eleccion==0:

            ContCrash=ContCrash+1
            if ContCrash==2:
                pygame.quit()
                

        # activado=True implica que tux no se mueva    
        activado = False

        if inkey==276: #Izquierda
            tux_pos_x = tux_pos_x - 10
            if tux_pos_x < 1 and activado==True:
                tux_pos_x = 640/2
        if inkey==275: #Derecha
            #print tux_pos_x
            tux_pos_x = tux_pos_x + 10
            if tux_pos_x > 560 and activado==True:
                tux_pos_x = 640/2
        if inkey==273: #Arriba
            tux_pos_y = tux_pos_y - 10
            eleccion=eleccion+1
            if tux_pos_y < 1 and activado==True:
                tux_pos_y = 200
        if inkey==274: #Abajo
            tux_pos_y = tux_pos_y + 10
            eleccion=eleccion-1
            if tux_pos_y > 400 and activado==True:
                tux_pos_y = 200


        #Aqui terminamos el programa y hacemos un return de la eleccion del usuario opcion elegida (enter en el teclado o mando)

        if inkey == 13:
            print "Se ha seleccionado la incicencia :" , Incidencias[eleccion]
            return Incidencias[eleccion]
            break
            #exit()

        #Aqui terminamos el programa por tecla esc

        if inkey == 27:
          print "Has crasheado el programa "
          break

          
        









if __name__ == "__main__":

    IncidenciaSeleccionada = main()

    #print DatosIniciales

    print "Fin del programa"

    #Enviamos los datos a telegram para mostrarlos en el movil

    TelegramBot.EnviarMensaje(DatosIniciales[0],DatosIniciales[1], IncidenciaSeleccionada)
