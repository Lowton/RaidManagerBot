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
    log.info('Вызвано приветствие ({})'.format(user.username))
    bot.send_message(chat_id=update.message.chat_id,
                     text=start_text)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Функция отключения бота
def off(bot, update):
    user = update.message.from_user
    log.info('Отключение бота ({})'.format(user.username))
    bot.send_message(chat_id=update.message.chat_id,
                     text="Выключаюсь…")
    updater.stop()

off_handler = CommandHandler('off', off)
dispatcher.add_handler(off_handler)

def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    log.info('{} прислал координаты: {}, {}'.format(user.username,
                                                   user_location.latitude,
                                                   user_location.longitude))
    update.message.reply_text("Координаты: {}, {}".format(user_location.latitude,user_location.longitude))

location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)



# Помощь
def help(bot, update):
    user = update.message.from_user
    help_text = "Справка.\nЭто заглушка для справки. Существут три команды:\n/start\n/help\n/off"
    log.info('Запрос справки ({})'.format(user.username))
    bot.send_message(chat_id=update.message.chat_id,
                     text=help_text)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

# записывает всё что прислали
def other(bot,update):
    user = update.message.from_user
    log.info('{} ({})'.format(update.message.text,user.username))
    update.message.reply_text("Не знаю как реагировать.")

other_handler = MessageHandler(Filters.text, other)
dispatcher.add_handler(other_handler)

# ответ на неизвестную команду
def unknown(bot,update):
    user = update.message.from_user
    log.info('Команда: {} ({})'.format(update.message.text,user.username))
    update.message.reply_text("Нет такой команды!")

# Задаём хендлер для всех остальных команд (заглушку)
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

#Запускаем бота
updater.start_polling()
