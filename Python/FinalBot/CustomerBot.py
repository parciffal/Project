import CUstumerdbCon
import telebot
from telebot import types
from config import *

bot = telebot.TeleBot(token='988779233:AAEWzRnjmFMi7nZ60As5boVgTsnwk5zJuFk')
dc = CUstumerdbCon.UserRegister
user_data = {}


def secondstep(message):
    user_data['couchname'] = message.text
    dc = CUstumerdbCon.UserRegister(user_data['name'], user_data['couchname'])
    dc.add_herba_user()
    b1 = types.InlineKeyboardButton('EJERCICIOS 🏋', callback_data='yes1')
    b2 = types.InlineKeyboardButton('🔥INTERMEDIOS', callback_data='yes2')
    b3 = types.InlineKeyboardButton('🚀AVANZADOS', callback_data='yes3')
    b4 = types.InlineKeyboardButton('RECETAS 🥗', callback_data='yes4')
    markup = types.InlineKeyboardMarkup()
    markup.add(b1)
    markup.add(b2)
    markup.add(b3)
    markup.add(b4)
    bot.send_message(message.chat.id, 'button message', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['one1', 'one2', 'one3', 'one4', 'one5'])
def callback_inlinemone(call):
    try:
        if call.message:
            if call.data == 'one1':
                textq = str(button1)
                bot.send_message(call.message.chat.id, 'DEL CULTIVO A LA MESA')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'one2':
                textq = str(button12)
                bot.send_message(call.message.chat.id, 'INTRODUCCIÓN: FILOSOFÍA GLOBAL DE NUTRICIÓN')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'one3':
                textq = str(button13)
                bot.send_message(call.message.chat.id, 'ENTENDIENDO LA NUTRICIÓN: MACRO Y MICRONUTRIENTES')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'one4':
                textq = str(button14)
                bot.send_message(call.message.chat.id, 'LA SALUD DEL CORAZÓN')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'one5':
                textq = str(button15)
                bot.send_message(call.message.chat.id, 'DRA. ROCÍO MEDINA: IMPORTANCIA DEL DESAYUNO')
                bot.send_message(call.message.chat.id, textq)
    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['two1','two2','two3','two4','two5','two6','two7','two8','two9', 'two10', 'two11', 'two12'])
def callback_inlinetwo(call):
    try:
        if call.message:
            if call.data == 'two1':
                textq = str(button21)
                bot.send_message(call.message.chat.id, 'PRIMEROS PASOS EN EL NEGOCIO')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two2':
                textq = str(button22)
                bot.send_message(call.message.chat.id, 'METAS Y PLAN DE ACCIÓN')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two3':
                textq = str(button23)
                bot.send_message(call.message.chat.id, 'PLAN DE MERCADEO CON EDGAR BALBÁS-ESPAÑOL')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two4':
                textq = str(button24)
                bot.send_message(call.message.chat.id,
                                 'PLAN DE MERCADEO 1: ¿CÓMO SE GANA DINERO? JHON TARTOL CLUB CHAIRMANS')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two5':
                textq = str(button25)
                bot.send_message(call.message.chat.id,
                                 'PLAN DE MERCADEO 2: ¿CÓMO SE GANA DINERO? JHON TARTOL CLUB CHAIRMANS')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two6':
                textq = str(button26)
                bot.send_message(call.message.chat.id, '¿CÓMO HACER UNA PRESENTACIÓN DE PRODUCTO?')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two7':
                textq = str(button27)
                bot.send_message(call.message.chat.id, '¿CÓMO HACER UN HOM?')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two8':
                textq = str(button28)
                bot.send_message(call.message.chat.id, '¿CÓMO HACER UNA PRESENTACIÓN VIRTUAL?')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two9':
                textq = str(button29)
                bot.send_message(call.message.chat.id, 'AVANZA CON LOS RETOS DE 21 DÍAS')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'two10':
                textq = str(button210)
                bot.send_message(call.message.chat.id, 'PROCESO DE REGISTRO ONLINE A LAS PERSONAS')
                bot.send_message(call.message.chat.id, textq)
    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['thr1' ,'thr2' ,'thr3'])
def callback_inlinethree(call):
    try:
        if call.message:
            if call.data == 'thr1':
                bot.send_message(call.message.chat.id, 'HERRAMIENTAS DE RECLUTAMIENTO')
                bot.send_message(call.message.chat.id, 'https://youtu.be/JCd1NAo2P7Q')
            elif call.data == 'thr2':
                textq = str(button32)
                bot.send_message(call.message.chat.id, 'TUTORIAL: ESTO ES HERBALIFE NUTRITION!')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'thr3':
                textq = str(button33)
                bot.send_message(call.message.chat.id, '¿CÓMO EXPANDIR TU LISTA EN REDES SOCIALES?')
                bot.send_message(call.message.chat.id, textq)

    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['fr1' ,'fr2' ,'fr3'])
def callback_inlinefour(call):
    try:
        if call.message:
            if call.data == 'fr1':
                textq = str(button41)
                bot.send_message(call.message.chat.id, 'HERRAMIENTAS COMERCIALES')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'fr2':
                textq = str(button42)
                bot.send_message(call.message.chat.id, '¿CÓMO HACER PEDIDOS EN MYHERBALIFE SAMCAM?')
                bot.send_message(call.message.chat.id, textq)
            elif call.data == 'fr3':
                textq = str(button43)
                bot.send_message(call.message.chat.id, '¿CÓMO HACER UN PEDIDO EN LÍNEA DIRECTAMENTE')
                bot.send_message(call.message.chat.id, textq)


    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['yes1', 'yes2', 'yes3', 'yes4'])
def callback_inlinem(call):
    try:
        if call.message:
            if call.data == 'yes1':
                a1 = types.InlineKeyboardButton('💯PRINCIPIANTES',callback_data='two1')
                a2 = types.InlineKeyboardButton('CALENTAMIENTO', callback_data='two2')
                a3 = types.InlineKeyboardButton('CARDIOVASCULAR', callback_data='two3')
                a4 = types.InlineKeyboardButton('ABDOMINALES 1', callback_data='two4')
                a5 = types.InlineKeyboardButton('ABDOMINALES 2', callback_data='two5')
                a6 = types.InlineKeyboardButton('TREN SUPERIOR 1',callback_data='two6')
                a7 = types.InlineKeyboardButton('TREN SUPERIOR 2', callback_data='two7')
                a8 = types.InlineKeyboardButton('TREN INFERIOR 1', callback_data='two8')
                a9 = types.InlineKeyboardButton('TREN INFERIOR 2', callback_data='two9')
                a10 = types.InlineKeyboardButton('ZONA MEDIA 1', callback_data='two10')
                a11 = types.InlineKeyboardButton('ZONA MEDIA 2', callback_data='two11')
                a12 = types.InlineKeyboardButton('FULL BODY 1', callback_data='two12')
                a13 = types.InlineKeyboardButton('FULL BODY 2', callback_data='two13')
                markyes = types.InlineKeyboardMarkup()
                markyes.add(a1)
                markyes.add(a2)
                markyes.add(a3)
                markyes.add(a4)
                markyes.add(a5)
                markyes.add(a6)
                markyes.add(a7)
                markyes.add(a8)
                markyes.add(a9)
                markyes.add(a10)
                markyes.add(a11)
                markyes.add(a12)
                markyes.add(a13)
                #b1 = types.InlineKeyboardButton('EJERCICIOS 🏋', callback_data='yes1')
                b2 = types.InlineKeyboardButton('🔥INTERMEDIOS', callback_data='yes2')
                b3 = types.InlineKeyboardButton('🚀AVANZADOS', callback_data='yes3')
                b4 = types.InlineKeyboardButton('RECETAS 🥗', callback_data='yes4')
                #markyes.add(b1)
                markyes.add(b2)
                markyes.add(b3)
                markyes.add(b4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
            elif call.data == 'yes2':
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('CARDIOVASCULARES', callback_data='one1')
                butt2 = types.InlineKeyboardButton('TREN SUPERIOR', callback_data='one2')
                butt3 = types.InlineKeyboardButton('TREN INFERIOR', callback_data='one3')
                butt4 = types.InlineKeyboardButton('ZONA MEDIA', callback_data= 'one4')
                butt5 = types.InlineKeyboardButton('FULL BODY', callback_data='one5')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                b1 = types.InlineKeyboardButton('EJERCICIOS 🏋', callback_data='yes1')
                #b2 = types.InlineKeyboardButton('🔥INTERMEDIOS', callback_data='yes2')
                b3 = types.InlineKeyboardButton('🚀AVANZADOS', callback_data='yes3')
                b4 = types.InlineKeyboardButton('RECETAS 🥗', callback_data='yes4')
                markyes.add(b1)
                #markyes.add(b2)
                markyes.add(b3)
                markyes.add(b4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
            elif call.data == 'yes3':
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('DESARROLLAR PECHO Y ESPALDA', callback_data='thr1')
                butt2 = types.InlineKeyboardButton('FORTALECER LA ZONA MEDIA', callback_data='thr2')
                butt3 = types.InlineKeyboardButton('DESARROLLAR BRAZOS Y HOMBROS', callback_data='thr3')
                butt4 = types.InlineKeyboardButton('ABDOMINALES Y GLÚTEOS', callback_data='thr4')
                butt5 = types.InlineKeyboardButton('FULL BODY', callback_data='thr5')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                b1 = types.InlineKeyboardButton('EJERCICIOS 🏋', callback_data='yes1')
                b2 = types.InlineKeyboardButton('🔥INTERMEDIOS', callback_data='yes2')
                #b3 = types.InlineKeyboardButton('🚀AVANZADOS', callback_data='yes3')
                b4 = types.InlineKeyboardButton('RECETAS 🥗', callback_data='yes4')
                markyes.add(b1)
                markyes.add(b2)
                #markyes.add(b3)
                markyes.add(b4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
            elif call.data == 'yes4':
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('ENSALADA DE ATÚN CON AGUACATE', callback_data='four1')
                butt2 = types.InlineKeyboardButton('ENSALADA DE ATÚN CON SALSA TZATZIKI', callback_data='four2')
                butt3 = types.InlineKeyboardButton('HUEVOS ALCACHOFADOS', callback_data='four3')
                butt4 = types.InlineKeyboardButton('LENTEJAS AL LIMÓN', callback_data='four4')
                butt5 = types.InlineKeyboardButton('GARBANZOS ASADOS PICANTES', callback_data='four5')
                butt6 = types.InlineKeyboardButton('PANECILLOS', callback_data='four6')
                butt7 = types.InlineKeyboardButton('PATATAS DULCES HORNEADAS CON NUECES', callback_data='four7')
                butt8 = types.InlineKeyboardButton('PESCADO AL HORNO', callback_data='four8')
                butt9 = types.InlineKeyboardButton('RISOTTO DE COLIFLOR', callback_data='four9')
                butt10 = types.InlineKeyboardButton('TACOS DE PAVO', callback_data='four10')
                butt11 = types.InlineKeyboardButton('SOPA DE POLLO CON VERDURAS', callback_data='four11')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                markyes.add(butt6)
                markyes.add(butt7)
                markyes.add(butt8)
                markyes.add(butt9)
                markyes.add(butt10)
                markyes.add(butt11)
                b1 = types.InlineKeyboardButton('EJERCICIOS 🏋', callback_data='yes1')
                b2 = types.InlineKeyboardButton('🔥INTERMEDIOS', callback_data='yes2')
                b3 = types.InlineKeyboardButton('🚀AVANZADOS', callback_data='yes3')
                #b4 = types.InlineKeyboardButton('RECETAS 🥗', callback_data='yes4')
                markyes.add(b1)
                markyes.add(b2)
                markyes.add(b3)
                #markyes.add(b4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['registr'])
def callback_inline(call):

    try:
        if call.message:
            if call.data == 'registr':
                bot.send_message(call.message.chat.id, 'vale emprecemos')
                bot.send_message(call.message.chat.id, 'NOMBRE Y APELLIDO')
                @bot.message_handler(content_types=['text'])
                def firststep(message):
                    user_data['name'] = message.text
                    msg = bot.send_message(message.chat.id, 'Nombre de tu coach:')
                    bot.register_next_step_handler(msg, secondstep)

    except Exception as e:
        print(repr(e))



@bot.message_handler(commands=['start'])
def start_message(message):
    butt_reg = types.InlineKeyboardButton('Registrate',callback_data='registr')
    markup = types.InlineKeyboardMarkup()
    markup.add(butt_reg)
    bot.send_message(message.chat.id, ("👋¡Hola {username}.\n!, un gusto saludarte! \n"
                                       "Te damos la bienvenida a nuestro canal de \n"
                                       "Telegram, en el cual te brindaremos rutinas \n"
                                       "de ejercicios🏋, ideas de recetas saludables 🥗\n"
                                       " y muchas cosas más 🤩").format(
        username=message.from_user.username), reply_markup=markup)




bot.polling(none_stop=True, interval=0)
