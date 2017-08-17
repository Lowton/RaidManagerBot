from telegram import (ReplyKeyboardMarkup,
                      ReplyKeyboardRemove,
                      KeyboardButton)
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters,
                          RegexHandler, ConversationHandler)
from log import log
import config

LEVEL, BOSS, LOCATION, INFO, TIME, CHECK = range(6)

# При старте
def start(bot, update):
    start_text = 'Бот предназначен для организиции рейдов '
    'на боссов игроков PokemonGO.\n'
    'Для создания рейда нажми /raid'
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
    return LEVEL
    
def not_raid_level(bot, update):
    user = update.message.from_user
    log.info('Затупил с выбором уровня рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_level,5)
    update.message.reply_text('Не так. Просто нажми на кнопку!',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
    return LEVEL
    
def raid_1(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_one,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
    return BOSS
    
def raid_2(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_two,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
    return BOSS
    
def raid_3(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_three,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
    return BOSS
    
def raid_4(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_four,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
    return BOSS

def raid_5(bot, update):
    user = update.message.from_user
    log.info('Тип рейда ({})'.format(user.username))
    reply_keyboard = build_menu(config.raid_leg,2)
    update.message.reply_text('Кто босс?',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
    return BOSS

def not_boss(bot, update):
    user = update.message.from_user
    log.info('Затупил с выбором босса ({})'.format(user.username))
    update.message.reply_text('Это не верный ответ! Кто босс? (выбери на кнопке)')

    return BOSS

def raid_boss(bot, update):
    user = update.message.from_user
    log.info('Рейд босс: {} ({})'.format(update.message.text,user.username))
    update.message.reply_text('Босс: {}\nОтправьте местоположение стадиона с рейдом.'.format(update.message.text),
                              reply_markup=ReplyKeyboardRemove())

    return LOCATION

def not_location(bot, update):
    user = update.message.from_user
    log.info('Затупил с геометкой({})'.format(user.username))
    update.message.reply_text('Отправьте геометку расположения стадиона с рейдом.')

    return LOCATION

# определение координат
def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    log.info('Координаты: {}, {} ({})'.format(user_location.latitude,
                                              user_location.longitude,
                                              user.username))
    update.message.reply_text("Координаты: {}, {}.\n"
                              "Чтобы другим тренерам было понятно где искать, "
                              "введите короткое описание арены".format(user_location.latitude,
                                                                       user_location.longitude))

    return INFO

def raid_info(bot, update):
    user = update.message.from_user
    log.info('Описание рейда: {} ({})'.format(update.message.text,user.username))
    update.message.reply_text("Инфа о рейде: {}. Введите оставшееся время рейда в формате Ч:ММ".format(update.message.text))

    return TIME

def not_info(bot, update):
    user = update.message.from_user
    log.info('Затупил с описанием  рейда: {} ({})'.format(update.message.text,
                                                          user.username))
    update.message.reply_text("Инфа о рейде: {}".format(update.message.text))

    return INFO
    
def raid_time(bot, update):
    user = update.message.from_user
    log.info('Время рейда: {} ({})'.format(update.message.text,user.username))
    reply_keyboard = build_menu(config.check_menu,2)
    update.message.reply_text("Спасибо за информацию. Всё верно? "
                              "Отсылаем приглашения?",
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))

    return CHECK

def not_time(bot, upgrade):
    user = update.message.from_user
    log.info('Затупил со временем рейда: {} ({})'.format(update.message.text,
                                                         user.username))
    update.message.reply_text("Время указано не в том формате. "
                              "Следует указать в формате Ч:ММ")

    return TIME

def raid_done(bot, update):
    user = update.message.from_user
    log.info('Завершил создание рейда ({})'.format(user.username))
    update.message.reply_text("`Рейд создан`\n"
                              "Босс *{boss}*\n\n"
                              "Доступен до {time}\n"
                              "Описание арены: {raid}\n\n"
                              "Координаты арены: {lat},{lon}"
                              "Кто пойдёт: "
                              "\n\n#{level} #{boss} #{player}".format(level='5',
                                                                      boss='Lugia',
                                                                      time='20:15',
                                                                      raid='На паравозе в шестом',
                                                                      lat=''
                                                                  
                                                                
                                                                  player=user.username),
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def not_done(bot,update):
    user = update.message.from_user
    log.info('Затупил с подтверждением ({})'.format(user.username))
    reply_keyboard = build_menu(config.check_menu,2)
    update.message.reply_text("Тут надо выбрать одну из двух кнопок",
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               resize_keyboard=True,
                                                               one_time_keyboard=True))
    

def cancel_raid(bot, update):
    user = update.message.from_user
    log.info("Создание рейда отменено ({})".format(user.first_name))
    update.message.reply_text('Создание рейда отменено.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

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

def regexp_all_boss():
    boss_list = ''
    for i in config.raid_one:
        boss_list += '|' + str(i)
    for i in config.raid_two:
        boss_list += '|' + str(i)
    for i in config.raid_three:
        boss_list += '|' + str(i)
    for i in config.raid_four:
        boss_list += '|' + str(i)
    for i in config.raid_leg:
        boss_list += '|' + str(i)

    # отрезаем лишний |
    boss_list = boss_list[1:len(boss_list)]
    log.info(boss_list)        

    return boss_list
    

def main():
    log.info('Бот запущен.')

    updater = Updater(token=config.token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('off', off))
    dp.add_handler(CommandHandler('help', help))
    all_boss_list = '^(' + regexp_all_boss() + ')$'

    # Хэндлер диалога по рейду
    raid_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('raid', new_raid)],

        states={
            LEVEL: [RegexHandler('^(1️⃣)$', raid_1),
                   RegexHandler('^(2️⃣)$', raid_2),
                   RegexHandler('^(3️⃣)$', raid_3),
                   RegexHandler('^(4️⃣)$', raid_4),
                   RegexHandler('^(5️⃣)$', raid_5),
                   MessageHandler(Filters.all, not_raid_level)],

            BOSS: [RegexHandler(all_boss_list, raid_boss),
                   MessageHandler(Filters.all, not_boss)],

            LOCATION: [MessageHandler(Filters.location, location),
                       MessageHandler(Filters.all, not_location)],

            INFO: [MessageHandler(Filters.text, raid_info),
                   MessageHandler(Filters.all, not_info)],

            TIME: [RegexHandler('^([0-1]:[0-5]\d)$', raid_time),
                   MessageHandler(Filters.all, not_time)],

            CHECK: [RegexHandler('^(✅)$', raid_done),
                    RegexHandler('^(❌)$', cancel_raid),
                    MessageHandler(Filters.all, not_done)]
            },

        fallbacks=[CommandHandler('cancel', cancel_raid)]
    )
    

    dp.add_handler(raid_conv_handler)

    dp.add_handler(MessageHandler(Filters.text, other))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
