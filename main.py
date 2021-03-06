import telebot

import os
import random

token = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(token)

# Заготовки предложений
first = ["Сегодня — идеальный день для новых начинаний. ",
         "Оптимальный день для того, чтобы решиться на смелый поступок! ",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние. ",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми. ",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами. "]

second = ["Но помните, что даже в этом случае нужно не забывать про",
          "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

second_add = [" отношения с друзьями и близкими. ",
              " работу и деловые вопросы, которые могут так некстати помешать планам. ",
              " себя и своё здоровье, иначе к вечеру возможен полный раздрай. ",
              " бытовые вопросы — особенно те, которые вы не доделали вчера. ",
              " отдых, чтобы не превратить себя в загнанную лошадь в конце месяца. "]

third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно. ",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

# Пишем бота.
@bot.message_handler(content_types=['text'])

# Реагируем на "Привет".
def get_text_message(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, сейчас я покажу тебе гороскоп на сегодня.")

        # Создаем и добавляем кнопки.
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_oven = telebot.types.InlineKeyboardButton(text="Овен", callback_data="zodiac")
        key_telec = telebot.types.InlineKeyboardButton(text="Телец", callback_data="zodiac")
        key_bliznecy = telebot.types.InlineKeyboardButton(text="Близнецы", callback_data="zodiac")
        key_rak = telebot.types.InlineKeyboardButton(text="Рак", callback_data="zodiac")
        key_lev = telebot.types.InlineKeyboardButton(text="Лев", callback_data="zodiac")
        key_deva = telebot.types.InlineKeyboardButton(text="Дева", callback_data="zodiac")
        key_vesy = telebot.types.InlineKeyboardButton(text="Весы", callback_data="zodiac")
        key_scorpion = telebot.types.InlineKeyboardButton(text="Скорпион", callback_data="zodiac")
        key_strelec = telebot.types.InlineKeyboardButton(text="Стрелец", callback_data="zodiac")
        key_kozerog = telebot.types.InlineKeyboardButton(text="Козерог", callback_data="zodiac")
        key_vodoley = telebot.types.InlineKeyboardButton(text="Водолей", callback_data="zodiac")
        key_ryby = telebot.types.InlineKeyboardButton(text="Рыбы", callback_data="zodiac")

        keyboard.add(key_oven)
        keyboard.add(key_telec)
        keyboard.add(key_bliznecy)
        keyboard.add(key_rak)
        keyboard.add(key_lev)
        keyboard.add(key_deva)
        keyboard.add(key_vesy)
        keyboard.add(key_scorpion)
        keyboard.add(key_strelec)
        keyboard.add(key_kozerog)
        keyboard.add(key_vodoley)
        keyboard.add(key_ryby)

        bot.send_message(message.from_user.id, "Выбери свой знак зодиака: ", reply_markup=keyboard)

    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши "Привет" :)')
    else:
        bot.send_message(message.from_user.id, 'Таких команд я еще не знаю. Напиши /help, чтобы узнать, что я умею.')
# Добавляем обработчик нажатий.

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'zodiac':
        bot.send_message(call.message.chat.id, random.choice(first) + random.choice(second) +
                         random.choice(second_add) + random.choice(third))

bot.polling(none_stop=True)
