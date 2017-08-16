from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters)
from log import log
import config

# При старте
def start(bot, update):
    start_text = 'Бот предназначен для организиции рейдов на боссов игроков PokemonGO.\n'
    user = update.message.from_user
    log.info('Вызвано приветствие ({})'.format(user.username))
    bot.send_message(chat_id=update.message.chat_id,
                     text=start_text)

# Функция отключения бота
def off(bot, update):
    user = update.message.from_user
    log.info('Отключение бота ({})'.format(user.username))
    bot.send_message(chat_id=update.message.chat_id,
                     text="Выключаюсь…")
    updater.stop()

# определение координат
def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    log.info('Координаты: {}, {} ({})'.format(user_location.latitude,
                                              user_location.longitude,
                                              user.username))
    update.message.reply_text("Координаты: {}, {}".format(user_location.latitude,
                                                          user_location.longitude))

# Помощь
def help(bot, update):
    user = update.message.from_user
    help_text = "Справка.\nЭто заглушка для справки. Существут три команды:\n/start\n/help\n/off"
    log.info('Запрос справки ({})'.format(user.username))
    bot.send_message(chat_id=update.message.chat_id,
                     text=help_text)

# записывает всё что прислали
def other(bot,update):
    user = update.message.from_user
    log.info('{} ({})'.format(update.message.text,user.username))
    update.message.reply_text("Не знаю как реагировать.")

# ответ на неизвестную команду
def unknown(bot,update):
    user = update.message.from_user
    log.info('Команда: {} ({})'.format(update.message.text,user.username))
    update.message.reply_text("Нет такой команды!")


def main():
    log.info('Бот запущен.')

    updater = Updater(token=config.token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('off', off))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.location, location))
    dp.add_handler(MessageHandler(Filters.text, other))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
