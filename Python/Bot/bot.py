import database
import telebot
from telebot import types
from config import TOKEN
import config

bot = telebot.TeleBot(token=TOKEN)
dataconnector = database.DataConnector()


@bot.message_handler(commands=['start'])
def start_message(message):
    butt1 = types.KeyboardButton('Subscribe')
    butt2 = types.KeyboardButton("Unsubscribe")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=4)
    markup.add(butt1)
    markup.add(butt2)
    dataconnector.add_user(message.from_user.username, message.from_user.id, False)
    bot.send_message(message.chat.id, ("Welcome {username}.\n I am the Assistant Bot of Lifetimeteam, "
                                       " where we will guide you step by step how to take your first steps,"
                                       "  together withg your sponsor and with the virtual system, "
                                       " to progress month by month and achieve the goals you set for yourself in the deal").format(
        username=message.from_user.username), reply_markup=markup)



@bot.message_handler(commands="Subscribe")
def subscribe(message):
    id = message.from_user.id
    if dataconnector.id_cheaker(id) == False:
        dataconnector.make_userActive(id)
        bot.send_message(message.chat.id, 'You succesfully Subscribed')
    else:
        bot.send_message(message.chat.id, 'You already Subscribed')


@bot.message_handler(commands="Unsubscribe")
def unsubscibe(message):
    id = message.from_user.id

    bot.send_message(message.chat.id, 'You sudenly Unsubscribed')
    if dataconnector.id_cheaker(id) == True:
        dataconnector.make_userNotActive(id)
        bot.send_message(message.chat.id, 'You sudenly Unsubscribed')
    else:
        bot.send_message(message.chat.id, 'You are not subscribed But we can change it')


bot.polling(none_stop=True)
