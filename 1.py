import telebot
import sqlite3

bot = telebot.TeleBot('1888213356:AAH7DXktdBnOSC_WmQ8miLoAMGGxtatR0Bc')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    defaut_name = "no name"
    username = defaut_name
    con = sqlite3.connect('db.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT name FROM users WHERE id = ' + str(message.from_user.id))
    rows = cursorObj.fetchall()
    if len(rows) > 0:
        username = rows[0][0]
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, " + username + ", чем я могу тебе помочь?")
    elif message.text == '/help':
        bot.send_message(message.from_user.id, str(message.from_user.id) + ", напиши привет")
    elif message.text[:5] == "/name":
        cursorObj = con.cursor()
        if username == defaut_name:
            cursorObj.execute('INSERT INTO users (id, name) values (' + str(message.from_user.id) + ', \'' + message.text[6:] + '\';')
        else:
            cursorObj.execute(
                'UPDATE users set name = \'' + message.text[6:] + '\' WHERE id = ' + str(message.from_user.id) + ';')
        con.commit()
        username = message.text[6:]
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
