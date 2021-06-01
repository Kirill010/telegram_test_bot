# игра загадочный шарик

import telebot
from random import choice
import sqlite3

bot = telebot.TeleBot('1888213356:AAH7DXktdBnOSC_WmQ8miLoAMGGxtatR0Bc')

choices = [
        'Бесспорно',
        'Предрешено',
        'Никаких сомнений',
        'Определённо да',
        'Можешь быть уверен в этом',
        'Мне кажется - «да»',
        'Вероятнее всего',
        'Хорошие перспективы',
        'Знаки говорят — «да»',
        'Да',
        'Пока не ясно, попробуй снова',
        'Спроси позже',
        'Лучше не рассказывать',
        'Сейчас нельзя предсказать',
        'Соберись и спроси опять',
        'Даже не думай',
        'Мой ответ — «нет»',
        'По моим данным — «нет»',
        'Перспективы не очень хорошие',
        'Весьма сомнительно',
    ]


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    username = "no name"
    global choices
    con = sqlite3.connect('db.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name FROM users WHERE id = ' + str(message.from_user.id))
    rows = cursorObj.fetchall()
    if len(rows) > 0:
        username = rows[0][0]
    if message.text == '/help':
        bot.send_message(message.from_user.id, username + ", напиши привет")
    elif message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, " + username + ", чем я могу тебе помочь?")
    elif message.text == "шар":
        bot.send_message(message.from_user.id, "Что вы хотите узнать?")
        tt = message.text
        ans = choice(choices)
        if tt[-1] == "?":
            bot.send_message(message.from_user.id, "Я думаю" + ans)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)



'''import sqlite3

con = sqlite3.connect('db.db')
cursorObj = con.cursor()
cursorObj.execute('SELECT * FROM users')
rows = cursorObj.fetchall()
for row in rows:
    print(row)'''