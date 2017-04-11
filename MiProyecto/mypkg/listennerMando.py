#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Pines de la Rrpi vvc 5v- Gnd Gnd Data en Gpio 17
"""
import lirc

sockid=lirc.init('appleremote', blocking =False)

Teclas={"KEY_0":0, "KEY_1":1, "KEY_2":2, "KEY_3":3, "KEY_4":4, "KEY_5":5, "KEY_6":6, "KEY_7":7, "KEY_8":8, "KEY_9":9, "KEY_UP":"UP", "KEY_LEFT":"LEFT", "KEY_RIGHT":"RIGHT","KEY_DOWN":"DOWN", "KEY_ENTER":"ENTER"}


#A = "KEY_0"
#print Teclas[A]
"""
"""
Variables configuradas
KEY_1
KEY_2
KEY_3
KEY_4
KEY_5
KEY_6
KEY_7
KEY_8
KEY_9
KEY_0
KEY_UP
KEY_LEFT
KEY_RIGHT
KEY_DOWN
KEY_ENTER
"""



def infoMando():

    while True:
        CodeIR = lirc.nextcode()
        if CodeIR !=[]:
            return CodeIR[0]
            pass


def main():

    while True:
        print infoMando()
    
    print "Fin del ciclo"


__name__ = False
if __name__ == "__main__": main()



