from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters)
from log import log
import config


log.info('Бот запущен.')

updater = Updater(token=config.token)
dispatcher = updater.dispatcher

def start(bot, update):
    start_text = 'Бот предназначен для организиции рейдов на боссов игроков PokemonGO.\n'
    user = update.message.from_user
    log.info('Вызвано приветствие (' + user.username + ')')
    bot.send_message(chat_id=update.message.chat_id,
                     text=start_text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Функция отключения бота
def off(bot, update):
    user = update.message.from_user
    log.info('Отключение бота (' + user.username + ')')
    bot.send_message(chat_id=update.message.chat_id,
                     text="Выключаюсь…")
    updater.stop()

off_handler = CommandHandler('off', off)
dispatcher.add_handler(off_handler)



#Запускаем бота
updater.start_polling()
