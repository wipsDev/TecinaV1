#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import time
import listennerMando




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






def get_key():

  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):

  
  fontobject = pygame.font.Font(None,28) #tamano de la letra

  if len(message) != 0:

    screen.blit(fontobject.render(message, 1, (255,255,255)), ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))

  pygame.display.flip()


eleccion=400

def ask(screen, question):

  "ask(screen, question) -> answer"

  pygame.font.init()

  current_string = []

  display_box(screen, question + ": " + string.join(current_string,""))



  while 1:


    UsamosMando = False
        
    if UsamosMando == True:
      inkey = get_Mando_key()
      print inkey    
      UsamosMando = True
            
      Teclas = {"KEY_0":256, "KEY_1":257, "KEY_2":258, "KEY_3":259, "KEY_4":260, "KEY_5":261, "KEY_6":262, "KEY_7":263, "KEY_8":264, "KEY_9":265, "KEY_UP":273, "KEY_LEFT":276, "KEY_RIGHT":275,"KEY_DOWN":274, "KEY_ENTER":13}
      inkey = Teclas[inkey]
    else:
            
      inkey = get_key()



    ##Aqui los controles buscan la accion que tienen que realizar   

    #print inkey
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
      #print "backspace"
    elif inkey == K_RETURN:
      #print "Intro"
      #answer = ask(screen, "Your name")
      break
    elif inkey == K_MINUS:
      current_string.append("_")

    elif inkey <= 127:
      current_string.append(chr(inkey))

    if inkey == 27:
      print "Has crasheado el programa "
      break

    eleccion=400
       
    if inkey >= 256 and inkey < 266: #Operativizamos el pad numerico

      dic={256:"0",257:"1",258:"2",259:"3",260:"4",261:"5",262:"6",263:"7",264:"8",265:"9"}

      current_string.append(dic[inkey])

      eleccion = dic[inkey]
    
    if eleccion==0:

        ContCrash=ContCrash+1

        if ContCrash==2:

            pygame.quit()
    

    #time.sleep(1)




    display_box(screen, question + ": " + string.join(current_string,""))

  return string.join(current_string,"")

def main(textpreg):#Configuracion de la pantalla

  #screen = pygame.display.set_mode((320*3,240*3))

  #give me the best depth with a 640 x 480 windowed display
  screen = pygame.display.set_mode((640, 480))

  #give me the biggest 16-bit display available
  modes = pygame.display.list_modes(0)
  #print modes
 
  #Para mostrar los controles
  screen = pygame.display.set_mode(modes[0]) 

  #Para ocultar los controles
  screen = pygame.display.set_mode(modes[0], FULLSCREEN)




  #El original es ##  screen = pygame.display.set_mode((320*3,240*3))

  return ask(screen, textpreg)




##if __name__ == '__main__': main()









def PrimerasIncidencias():

    textpreg="Introduce tu numero de empleado"
    Text1 = main(textpreg)

    textpreg="Introduce la habitacion en la que estas"
    Text2 = main(textpreg)

    textpreg="Introduce la incidencia"
    Text3 = main(textpreg)

    ##    textpreg="Gracias por utilizar nuestro servicio ;)"
    ##    Text4 = main(textpreg)

    return (Text1, Text2, Text3)
    ##    pygame.quit()

##PrimerasIncidencias()


















"""
####################################
#
#De aqui solicitamos incidencia#####
#
####################################

def get_key():

  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, eleccion):
  
  fontobject = pygame.font.Font(None,40) #tamano de la letra



  Incidencias=["Cocina rota", "Baño roto", "Mando de televisión sin pilas", "Suelo roto", "Robaron Jabones", "Robaron dvd", "Se acabo el gas"]
  Cont=0
  Posibles=[0,130, 260, 390, 520, 650, 780]
  X=0
  for Incidencia in Incidencias:

    
    
    pygame.draw.rect(screen, (255,255,255), ((screen.get_width() / 2) - 102, (screen.get_height()-Posibles[eleccion]-100 ) - 40, 500,60), 1)  #1= Ancho de linea. Modifica hacia abajo, hacia arriba, derecha 
    X=X+1

    Cont=Cont+130
    screen.blit(fontobject.render(Incidencia, 1, (255,255,255)), ((screen.get_width() / 2) - 100, ( Cont+10) )) #ojo, no calcula la altura

    #screen.blit(fontobject1.render(message, 1, (255,255,255)), ((screen.get_width()/2 )- 100 , (screen.get_height()/2 )-10))
    
    pygame.display.update() #Esto dibuja en pantalla    
    #time.sleep(1)

  

def ask(screen, question):

  pygame.font.init()
  current_string = []
  eleccion=0
  display_box(screen, eleccion)


  while 1:
    inkey = get_key()
    print inkey
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
      #print "backspace"
    elif inkey == K_RETURN:
      #print "Intro"
      #answer = ask(screen, "Your name")
      break
    elif inkey == K_MINUS:
      current_string.append("_")

    elif inkey <= 127:
      current_string.append(chr(inkey))

    if inkey == 27:
      print "Has crasheado el programa "
      break

       
    if inkey >= 256 and inkey < 266:#Operativizamos el pad numerico
      dic={256:"0",257:"1",258:"2",259:"3",260:"4",261:"5",262:"6",263:"7",264:"8",265:"9"}
      dic1={256:0,257:1,258:2,259:3,260:4,261:5,262:6,263:7,264:8,265:9}
      eleccion = dic1[inkey]

      current_string.append(dic[inkey])
    

    #time.sleep(1)


    

    display_box(screen,eleccion)
  return string.join(current_string,"")

def main(textpreg):#Configuracion de la pantalla
  #screen = pygame.display.set_mode((320*3,240*3))

  #give me the best depth with a 640 x 480 windowed display
  screen = pygame.display.set_mode((640, 480))

  #give me the biggest 16-bit display available
  modes = pygame.display.list_modes(0)
  #print modes
  
  #Para ocultar los controles
  screen = pygame.display.set_mode(modes[0], FULLSCREEN)


  #Para mostrar los controles
  #screen = pygame.display.set_mode(modes[0])



  #El original es ##  screen = pygame.display.set_mode((320*3,240*3))

  return ask(screen, textpreg)





Incidencias=["Cocina rota", "Baño roto", "Mando de televisión sin pilas", "Suelo roto", "Robaron Jabones", "Robaron dvd", "Se acabo el gas"]





#for x in Incidencias:
respuesta = main("x")
"""
  













#answer = ask(screen, "Your name")







