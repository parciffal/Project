import database
import telebot
from telebot import types
from config import TOKEN
from config import *

bot = telebot.TeleBot(token=TOKEN)
dataconnector = database.DataConnector()

@bot.callback_query_handler(func=lambda call: call.data in ['yesone', 'yestwo','yesthree', 'yesfour', 'yesfive'])
def callback_inlinem(call):
    try:
        if call.message:
            if call.data == 'yesone':
                textq = str(YESVIDEO1)
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'yestwo':
                textq = str(YESVIDEO2)
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'yesthree':
                textq = str(YESVIDEO3)
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'yesfour':
                textq = str(YESVIDEO4)
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'yesfive':
                textq = str(YESVIDEO5)
                bot.send_message(call.message.chat.id, textq)

    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                markyes = types.InlineKeyboardMarkup( )
                butt1 = types.InlineKeyboardButton('Herbalife History', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('Multilevel Pyramid', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('Product', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('Multilevel Marketing (GoPro)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 pillars of Jim Rohn', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos for you', reply_markup=markyes)
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, 'Бывает ')

    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    id = message.from_user.id
    if dataconnector.id_cheaker(id) == False:
        dataconnector.make_userActive(id)
        bot.send_message(message.chat.id, 'You succesfully Subscribed')
    else:
        bot.send_message(message.chat.id, 'You already Subscribed')


@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    id = message.from_user.id
    if dataconnector.id_cheaker(id) == True:
        dataconnector.make_userNotActive(id)
        bot.send_message(message.chat.id, "You sudenly Unsubscribed")
    else:
        bot.send_message(message.chat.id, 'You are not Subscribed')


@bot.message_handler(commands=['start'])
def start_message(message):
    butt1 = types.KeyboardButton('/subscribe')
    butt2 = types.KeyboardButton('/unsubscribe')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=4)
    markup.add(butt1,butt2)
    dataconnector.add_user(message.from_user.username, message.from_user.id, False)
    bot.send_message(message.chat.id, ("Welcome {username}.\n I am the Assistant Bot of Lifetimeteam, "
                                       " where we will guide you step by step how to take your first steps,"
                                       "  together withg your sponsor and with the virtual system, "
                                       " to progress month by month and achieve the goals you set for yourself in the deal").format(
        username=message.from_user.username), reply_markup=markup)
    butt_yes = types.InlineKeyboardButton("Yes", callback_data='yes')
    butt_no = types.InlineKeyboardButton("No", callback_data='no')
    markup1 = types.InlineKeyboardMarkup(row_width=3)
    markup1.add(butt_yes, butt_no)
    bot.send_message(message.chat.id, 'Lets get started!!! Are you a new Distributor', reply_markup=markup1)


bot.polling(none_stop=True, interval=0)
