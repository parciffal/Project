import telebot
from telebot import types
import database
import hdatabase
from config import *

bot = telebot.TeleBot(token=ADMINTOKEN)
db = database.DataConnector()
hdat = hdatabase.UserRegister('asd','asd','sad','asd')


def deluser(message):
    try:
        db.remove(message.text)
        bot.send_message(message.chat.id, 'User deleted')
    except Exception as e :
        bot.send_message(message.chat.id, 'Wrong ID')
        print(repr(e))


def delHerbauser(message):
    try:
        hdat.remove(message.text)
        bot.send_message(message.chat.id, 'User deleted')
    except Exception as e :
        bot.send_message(message.chat.id, 'Wrong ID')
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['showusers', 'sendmess', 'showherba'])
def callback_inline(call):
    try:
        if call.data == 'showusers':
            users = db.get_users_rows()
            bot.send_message(SUBADMIN, 'base de datos de usuarios de bot')
            bot.send_message(SUBADMIN, str(users))
        elif call.data == 'sendmess':
            bot.send_message(SUBADMIN, 'Envíame un mensaje de texto para enviar')

            @bot.message_handler(content_types='text')
            def everyone(message):
                ids = db.get_all_ids()
                for i in ids:
                    bot.send_message(i, message.text)
                bot.send_message(SUBADMIN, 'Mensajes enviados')    
        elif call.data == 'showherba':
            bot.send_message(SUBADMIN, 'Base de datos de usuarios de Herbalife')
            bot.send_message(SUBADMIN, str(hdat.get_users_rows()))
        elif call.data == 'delherba':
            msg = bot.send_message(call.message.chat.id, 'Send me Herbalife ID of user')
            bot.register_next_step_handler(msg, deluser)
        elif call.data == 'deluser':
            msg = bot.send_message(call.message.chat.id, 'Send me id of Bot user')
            bot.register_next_step_handler(msg, delHerbauser)

    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['start'])
def starting(message):
    if str(message.from_user.id) == str(SUBADMIN):
        try:
            markup = types.InlineKeyboardMarkup()
            showallusers = types.InlineKeyboardButton('Mostrar todos los usuarios de bot', callback_data='showusers')
            sendmessage = types.InlineKeyboardButton('Enviar mensaje a todos los usuarios', callback_data='sendmess')
            showherbausers = types.InlineKeyboardButton('Mostrar usuarios de Herbalife', callback_data='showherba')
            deleteherbauser = types.InlineKeyboardButton('Delete Herbalife user', callback_data='delherba')
            deletebotuser = types.InlineKeyboardButton('Delete Bot user', callback_data='deluser')
            markup.add(showherbausers)
            #  markup.add(deleteherbauser)
            markup.add(showallusers)
            #markup.add(deletebotuser)
            markup.add(sendmessage)
            bot.send_message(message.chat.id, 'Hola entrenadora lo que hacemos hoy', reply_markup=markup)
        except Exception as e:
            print(repr(e))
    else:
        bot.send_message(message.chat.id, "Sorry it's not your's")

bot.polling(none_stop=True, interval=0)
