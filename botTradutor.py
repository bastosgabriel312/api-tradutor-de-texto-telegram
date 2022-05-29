import telebot
import os
import json
import requests
from tradutor import *

tokenTelegram = os.environ['TOKEN_TELEGRAM']
tokenTradutor = os.environ['TOKEN_TRADUTOR']
bot = telebot.TeleBot(tokenTelegram)
tradutor = Tradutor(tokenTradutor,'centralus')

def traduzirIdioma(mensagem):
    try:
        texto = mensagem.text.replace('/traduzir',"")
        print(texto)
        idioma = tradutor.detectarIdioma(texto)[0]['language']
        textoTraduzido = tradutor.traduzir(idioma, 'pt-br', texto)
        print(texto)
        return textoTraduzido['translations'][0]['text']
    except Exception:
        return "Ocorreu um erro inesperado, por gentileza contate o responsável"


@bot.message_handler(commands=["traduzir"])
def opcaoTraduzir(mensagem):
    retornoTraducao = traduzirIdioma(mensagem)
    bot.send_message(mensagem.chat.id, retornoTraducao)



####################### Inicia com essa mensagem ###################
@bot.message_handler()
def responder(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Ir até o repositório', url='https://github.com/bastosgabriel312/api-tradutor-telegram'
       )
   )
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Fale com um representante', url='telegram.me/bastosgabriel312'
       )
   )

   bot.send_message(
       message.chat.id,
       ' SEJA BEM VINDO AO TRADUTOR  \n\n' +
       '- Para traduzir envie /traduzir  e o texto que deseja traduzir\n'+
       '- Exemplo /traduzir hello world',
       reply_markup=keyboard
   )


# Executa bot em looping
bot.polling()