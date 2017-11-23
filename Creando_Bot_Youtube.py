import telegram
from telegram.ext import *

mi_bot = telegram.Bot(token="507775944:AAH3dUvglFi2NlpODeC0A8O85jtzQ-4m7Tg")
mi_bot_updater = Updater(mi_bot.token)


def listener(bot, update):
	id = update.message.chat_id
	mensaje = update.message.text
	print("ID: "+str(id) + " MENSAJE: " + mensaje)

def start(bot, update, pass_chat_data=True):
	update.message.chat_id
	bot.sendMessage(chat_id=update.message.chat_id, text="Gracias por usarme Gabriel!")

def gabo(bot, update, pass_chat_data=True):
	update.message.chat_id
	bot.sendMessage(chat_id=update.message.chat_id, text="Gabo")
	bot.sendMessage(chat_id=update.message.chat_id, text="Hola yo he creado este bot")


def lista_p1(bot, update, pass_chat_data=True):
	update.message.chat_id
	bot.sendMessage(chat_id=update.message.chat_id, text="German")
	bot.sendMessage(chat_id=update.message.chat_id, text="Alfonso")
	bot.sendMessage(chat_id=update.message.chat_id, text="Hiram")
	bot.sendMessage(chat_id=update.message.chat_id, text="Manuel")
	bot.sendMessage(chat_id=update.message.chat_id, text="Romina")
	bot.sendMessage(chat_id=update.message.chat_id, text="Sandra")
	bot.sendMessage(chat_id=update.message.chat_id, text="Lorena")
	bot.sendMessage(chat_id=update.message.chat_id, text="Ilse")



start_handler = CommandHandler('start', start)
gabo_handler = CommandHandler('gabo', gabo)
lista_p1_handler = CommandHandler('lista_p1', lista_p1)
listener_handler = MessageHandler(Filters.text, listener)

dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(gabo_handler)
dispatcher.add_handler(lista_p1_handler)
dispatcher.add_handler(listener_handler)

mi_bot_updater.start_polling()
mi_bot_updater.idle()


while True:
	pass