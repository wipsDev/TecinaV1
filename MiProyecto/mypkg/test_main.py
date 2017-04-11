#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php
# https://www.pythonmania.net/es/2010/03/25/tutorial-pygame-2-ventana-e-imagenes/


# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame, pygame.event
from pygame.locals import *
import sys
import time


# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------

 
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
 
pygame.init()
white = (255, 255, 255)
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

time.sleep(1)
color = (0, 0, 0)
text = Text()
ejey=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
    screen.fill(color)
    ejey=ejey+10
    text.render(screen, "HelloÑAÑEÑé Word!", white, (0, ejey))

    time.sleep(1)
    
    pygame.display.flip()