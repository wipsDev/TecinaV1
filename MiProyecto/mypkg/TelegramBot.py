# -*- coding: utf-8 -*-

import time
import telebot
import TokenAccess





commands = {  # command description used in the "help" command
              'start': 'Inicia el programa',
              'help': 'Ofrece informacion sobre los comandos disponibles',
              'Edgar': 'No hace nada',
              'Crash': 'Crashea el servico',
              'Author': 'Muestra el autor',
              'Crash2Script': 'Rompe el SegundoScript',
              'LimpiarCahe': 'Limpia la cache de la Raspberry',
              'Start2Script': 'Activa el segundo Script',
                       

}

"""
Instrucciones
Para responder comentando lo que se ha dicho, se utiliza
    bot.reply_to(message,"Hi")

Para enviar un mensaje se utiliza
bot.send_message(cid, "Hola desconocido, deja escanearte... ")

Para coger el mensaje de Telegram se utiliza

def handle_messages(messages):
    for message in messages:
        bot.reply_to(message,"He recibido este texto")
        print message.text

bot.set_update_listener(handle_messages)

"""


bot = telebot.TeleBot(TokenAccess.bot())
#bot.set_update_listener(listener)  # register listener

ident=TokenAccess.MiUser()





# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    bot.send_message(cid, "Hola desconocido, deja escanearte... ")
    time.sleep(4)
    msg = "Tu numero de usuario es: " + str(cid)
    bot.send_message(cid, msg)
    command_help(m)  # show the new user the help page

# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page
    


def EnviarMensaje(D1,D2,D3):

    Hora = time.strftime("%H:%M:%S")

    Mensaje=("El usuario ", D1, " acaba de poner una incicencia en la habitación ", D2, " En referencia a : ", D3, " a las ", Hora)

    Mensaje="".join(Mensaje)
    print Mensaje
    bot.send_message(ident, Mensaje)





##########
##########




def main():
    bot.send_message(ident,"Bot ejecutado!!")


if __name__ == "__main__":
    main()


print "Ejecucion Correcta!! "



## Este es el script que se ejectuta al arrancar la RRpi, se disena con la finalidad de ejecutar telebot
## y la medicion de la temperatura de mi casa al arrancar.
## El problema que soluciono en este script es el de ejecutar dos ciclos While true de forma simultanea
## Por un lado el que necesita Telebot para funcionar, y por otro lado el que neceita el sensor de temperatura para
## No dejar de funcionar. mi email edgar.hdezm@hotmail.com creado por Edgar Hernandez Molina

