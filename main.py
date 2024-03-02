
import  telebot
from Gemeni import Gemeni
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
GEMENI_TOKEN = os.environ.get('GEMENI_TOKEN', '')

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)
gemeni = Gemeni(token=GEMENI_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
     bot.reply_to(message, "Hola, soy tu bot de prueba")
     bot.reply_to(message, "Escribe /saludo para saludar")

@bot.message_handler(commands=['saludo'])
def send_saludo(message):
     bot.reply_to(message, "Hola, como estas?")


# capturar todos los mensajes que no sean comandos
@bot.message_handler(func=lambda message: True)
def echo_all(message):
     response = gemeni.generateContent(message.text)
     bot.reply_to(message, response)
     
if __name__ == '__main__':
     bot.polling(none_stop=True)

