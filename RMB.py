from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters,
                          RegexHandler)
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

# Заебеним динамичное меню
def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


def new_raid(bot, update):
    user = update.message.from_user
    log.info('Новый рейд ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_level,5)
    update.message.reply_text('Какой уровень рейда?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))

def raid_1(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_one,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
    
           
def raid_2(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_two,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
def raid_3(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_three,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
def raid_4(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_four,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
def raid_5(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_leg,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))

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
    dp.add_handler(CommandHandler('raid', new_raid))
    dp.add_handler(RegexHandler('^(1️⃣)$', raid_1))
    dp.add_handler(RegexHandler('^(2️⃣)$', raid_2))
    dp.add_handler(RegexHandler('^(3️⃣)$', raid_3))
    dp.add_handler(RegexHandler('^(4️⃣)$', raid_4))
    dp.add_handler(RegexHandler('^(5️⃣)$', raid_5))
    dp.add_handler(MessageHandler(Filters.location, location))
    dp.add_handler(MessageHandler(Filters.text, other))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
