import database
import hdatabase
import telebot
from telebot import types
from config import *

bot = telebot.TeleBot(token='988779233:AAEWzRnjmFMi7nZ60As5boVgTsnwk5zJuFk')
dataconnector = database.DataConnector()
user_data = {}

def laststep(message):
    user_data['couchname'] = message.text
    hd = hdatabase.UserRegister(user_data['name'],user_data['surname'],user_data['hid'],user_data['couchname'])
    hd.add_herba_user()
    butt_yes = types.InlineKeyboardButton("Si", callback_data='yes')
    butt_no = types.InlineKeyboardButton("NO", callback_data='no')
    markup1 = types.InlineKeyboardMarkup(row_width=3)
    markup1.add(butt_yes, butt_no)
    bot.send_message(message.chat.id, '💪 Agregaste tu información con éxito!!\n'
                                      '¡Empecemos! ¿Eres nuevo distribuidor?', reply_markup=markup1)


def therdstep(message):
    user_data['hid'] = message.text
    msg = bot.send_message(message.chat.id, 'Nombre de su patrocinador de Herbalife:')
    bot.register_next_step_handler(msg, laststep)

def secondstep(message):
    user_data['surname'] = message.text
    msg = bot.send_message(message.chat.id, 'Ingrese su identificacion de Herbalife')
    bot.register_next_step_handler(msg, therdstep)

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

@bot.callback_query_handler(func=lambda call: call.data in ['two1','two2','two3','two4','two5','two6','two7','two8','two9', 'two10'])
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


@bot.callback_query_handler(func=lambda call: call.data in ['thr1','thr2','thr3'])
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


@bot.callback_query_handler(func=lambda call: call.data in ['fr1','fr2','fr3'])
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


@bot.callback_query_handler(func=lambda call: call.data in ['yesone', 'yestwo', 'yesthree', 'yesfour', 'yesfive'])
def callback_inlinem(call):
    try:
        if call.message:
            if call.data == 'yesone':
                textq = str(YESVIDEO1)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                #butt1 = types.InlineKeyboardButton('HISTORIA DE HERBALIFE', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('PIRÁMIDE MULTINIVEL', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('PRODUCTO', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('MARKETING MULTINIVEL (GOPRO)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 PILARES DE JIM ROHN', callback_data='yesfive')
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
            elif call.data == 'yestwo':
                textq = str(YESVIDEO2)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('HISTORIA DE HERBALIFE', callback_data='yesone')
                #butt2 = types.InlineKeyboardButton('PIRÁMIDE MULTINIVEL', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('PRODUCTO', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('MARKETING MULTINIVEL (GOPRO)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 PILARES DE JIM ROHN', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
            elif call.data == 'yesthree':
                textq = str(YESVIDEO3)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('HISTORIA DE HERBALIFE', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('PIRÁMIDE MULTINIVEL', callback_data='yestwo')
                #butt3 = types.InlineKeyboardButton('PRODUCTO', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('MARKETING MULTINIVEL (GOPRO)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 PILARES DE JIM ROHN', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
            elif call.data == 'yesfour':
                textq = str(YESVIDEO4)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('HISTORIA DE HERBALIFE', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('PIRÁMIDE MULTINIVEL', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('PRODUCTO', callback_data='yesthree')
                #butt4 = types.InlineKeyboardButton('MARKETING MULTINIVEL (GOPRO)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 PILARES DE JIM ROHN', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
            elif call.data == 'yesfive':
                textq = str(YESVIDEO5)
                bot.send_message(call.message.chat.id, textq)
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('HISTORIA DE HERBALIFE', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('PIRÁMIDE MULTINIVEL', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('PRODUCTO', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('MARKETING MULTINIVEL (GOPRO)', callback_data='yesfour')
                #butt5 = types.InlineKeyboardButton('12 PILARES DE JIM ROHN', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['noone', 'notwo', 'notree', 'nofour'])
def callback_inlinem(call):
    try:
        if call.message:
            if call.data == 'noone':
                markno = types.InlineKeyboardMarkup()
                a1 = types.InlineKeyboardButton('DEL CULTIVO A LA MESA',callback_data='one1')
                a2 = types.InlineKeyboardButton('INTRODUCCIÓN: FILOSOFÍA GLOBAL DE NUTRICIÓN',callback_data= 'one2')
                a3 = types.InlineKeyboardButton('ENTENDIENDO LA NUTRICIÓN: MACRO Y MICRONUTRIENTES',callback_data='one3')
                a4 = types.InlineKeyboardButton('LA SALUD DEL CORAZÓN',callback_data='one4')
                a5 = types.InlineKeyboardButton('DRA. ROCÍO MEDINA: IMPORTANCIA DEL DESAYUNO',callback_data='one5')
                butt1 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE PRODUCTO', callback_data='noone')
                butt2 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE NEGOCIO', callback_data='notwo')
                butt3 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS DE APOYO',
                                                   callback_data='notree')
                butt4 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS COMERCIALES',
                                                   callback_data='nofour')
                markno.add(a1)
                markno.add(a2)
                markno.add(a3)
                markno.add(a4)
                markno.add(a5)
                markno.add(butt2)
                markno.add(butt3)
                markno.add(butt4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markno)
            elif call.data == 'notwo':
                a1 = types.InlineKeyboardButton('PRIMEROS PASOS EN EL NEGOCIO', callback_data='two1')
                a2 = types.InlineKeyboardButton('METAS Y PLAN DE ACCIÓN', callback_data='two2')
                a3 = types.InlineKeyboardButton('PLAN DE MERCADEO CON EDGAR BALBÁS-ESPAÑOL', callback_data='two3')
                a4 = types.InlineKeyboardButton('PLAN DE MERCADEO 1: ¿CÓMO SE GANA DINERO? JHON TARTOL CLUB CHAIRMANS', callback_data='two4')
                a5 = types.InlineKeyboardButton('PLAN DE MERCADEO 2: ¿CÓMO SE GANA DINERO? JHON TARTOL CLUB CHAIRMANS', callback_data='two5')
                a6 = types.InlineKeyboardButton('¿CÓMO HACER UNA PRESENTACIÓN DE PRODUCTO?', callback_data='two6')
                a7 = types.InlineKeyboardButton('¿CÓMO HACER UN HOM?', callback_data='two7')
                a8 = types.InlineKeyboardButton('¿CÓMO HACER UNA PRESENTACIÓN VIRTUAL?', callback_data='two8')
                a9 = types.InlineKeyboardButton('AVANZA CON LOS RETOS DE 21 DÍAS', callback_data='two9')
                a10 = types.InlineKeyboardButton('PROCESO DE REGISTRO ONLINE A LAS PERSONAS', callback_data='two10')
                markno = types.InlineKeyboardMarkup()
                markno.add(a1)
                markno.add(a2)
                markno.add(a3)
                markno.add(a4)
                markno.add(a5)
                markno.add(a6)
                markno.add(a7)
                markno.add(a8)
                markno.add(a9)
                markno.add(a10)
                butt1 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE PRODUCTO', callback_data='noone')
                butt2 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE NEGOCIO', callback_data='notwo')
                butt3 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS DE APOYO',
                                                   callback_data='notree')
                butt4 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS COMERCIALES',
                                                   callback_data='nofour')
                markno.add(butt1)
                markno.add(butt3)
                markno.add(butt4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markno)
            elif call.data == 'notree':
                a1 = types.InlineKeyboardButton('HERRAMIENTAS DE RECLUTAMIENTO',callback_data='thr1')
                a2 = types.InlineKeyboardButton('TUTORIAL: ESTO ES HERBALIFE NUTRITION!', callback_data='thr2')
                a3 = types.InlineKeyboardButton('¿CÓMO EXPANDIR TU LISTA EN REDES SOCIALES?', callback_data='thr3')
                markno = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE PRODUCTO', callback_data='noone')
                butt2 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE NEGOCIO', callback_data='notwo')
                butt3 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS DE APOYO',
                                                   callback_data='notree')
                butt4 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS COMERCIALES',
                                                   callback_data='nofour')
                markno.add(a1)
                markno.add(a2)
                markno.add(a3)
                markno.add(butt1)
                markno.add(butt2)
                markno.add(butt4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markno)
            elif call.data == 'nofour':
                a1 = types.InlineKeyboardButton('HERRAMIENTAS COMERCIALES', callback_data='fr1')
                a2 = types.InlineKeyboardButton('¿CÓMO HACER PEDIDOS EN MYHERBALIFE SAMCAM?', callback_data='fr2')
                a3 = types.InlineKeyboardButton('¿CÓMO HACER UN PEDIDO EN LÍNEA DIRECTAMENTE', callback_data='fr3')
                butt1 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE PRODUCTO', callback_data='noone')
                butt2 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE NEGOCIO', callback_data='notwo')
                butt3 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS DE APOYO',
                                                   callback_data='notree')
                butt4 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS COMERCIALES',
                                                   callback_data='nofour')
                markno = types.InlineKeyboardMarkup()
                markno.add(a1)
                markno.add(a2)
                markno.add(a3)
                markno.add(butt1)
                markno.add(butt2)
                markno.add(butt3)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markno)
    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no', 'registr', 'negyes', 'negno'])
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'yes':
                bot.send_message(call.message.chat.id, 'Es importante que sigas los siguientes pasos 👇\n'
                                                       '1) Asegúrate de estar en los grupos de WhatsApp y Facebook.\n'
                                                       '2) Descarga la aplicación Zoom Meetingg, la usarás para\n'
                                                       '   tus sesiones de entrenamiento.\n'
                                                       '3) Esta es una carrera, ¡así que debes estar ansioso por \n'
                                                       'aprender! \n'
                                                       'El material que te enviamos, lo estudiamos y desarrollamos,\n'
                                                       'lo bueno es que son cosas muy sencillas.\n'
                                                       '4) Estaremos aquí para apoyarlo, pero su éxito dependerá de \n'
                                                       'las decisiones que tome.\n\n'
                                                       '¿Te gustaron los videos? Espero que te haya sido muy util :fire:\n'
                                                       '🔥Proximamente te enviaremos más contenido por este medio')
                markyes = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('HISTORIA DE HERBALIFE', callback_data='yesone')
                butt2 = types.InlineKeyboardButton('PIRÁMIDE MULTINIVEL', callback_data='yestwo')
                butt3 = types.InlineKeyboardButton('PRODUCTO', callback_data='yesthree')
                butt4 = types.InlineKeyboardButton('MARKETING MULTINIVEL (GOPRO)', callback_data='yesfour')
                butt5 = types.InlineKeyboardButton('12 PILARES DE JIM ROHN', callback_data='yesfive')
                markyes.add(butt1)
                markyes.add(butt2)
                markyes.add(butt3)
                markyes.add(butt4)
                markyes.add(butt5)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markyes)
            elif call.data == 'no':
                bot.send_message(call.message.chat.id, '¡Excelente! Vamos al siguiente paso \n'
                                                       '🤩Antes de comenzar, necesitas dos cosas: \n'
                                                       '1)¡Tener Metas! ¿A dónde quieres llegar?  \n'
                                                       '¿Qué quieres lograr?¿Cuánto quieres ganar? \n'
                                                       '\n'
                                                       '2)Y saber ¿por qué estás haciendo este \n'
                                                       'negocio? ¿Cuál es tu propósito final? \n'
                                                       '¿Reemplazar tu trabajo? ¿Tienes más \n'
                                                       'tiempo con tu familia? ¿Cambiar vidas? \m'
                                                       '¿Viajar por el mundo? \n'
                                                       '\n'
                                                       '¡Escríbelo! Y así cuando tengas ganas \n'
                                                       'de darte por vencido, eso es lo que te \n'
                                                       'ayudará a seguir adelante 💪\n'
                                                       '\n'
                                                       'Si quieres escríbelas y déjalas acá,\n'
                                                       'así siempre te acordarás de esas \n'
                                                       'cosas por las que iniciaste en este \n'
                                                       'negocio, también compártelas con tu \n'
                                                       'patrocinador.')
                buttno1 = types.InlineKeyboardButton('SI', callback_data='negyes')
                buttno2 = types.InlineKeyboardButton('NO',callback_data='negno')
                markup = types.InlineKeyboardMarkup()
                markup.add(buttno1,buttno2)
                bot.send_message(call.message.chat.id, '¡Empecemos! 💪 ¿Eres nuevo distribuidor?', reply_markup=markup)
            elif call.data == 'negyes':
                markno = types.InlineKeyboardMarkup()
                butt1 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE PRODUCTO', callback_data='noone')
                butt2 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE NEGOCIO', callback_data='notwo')
                butt3 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS DE APOYO', callback_data='notree')
                butt4 = types.InlineKeyboardButton('QUIERO SABER MÁS SOBRE HERRAMIENTAS COMERCIALES', callback_data='nofour')
                markno.add(butt1)
                markno.add(butt2)
                markno.add(butt3)
                markno.add(butt4)
                bot.send_message(call.message.chat.id, 'Videos para ti', reply_markup=markno)
            elif call.data == 'negno':
                bot.send_message(call.message.chat.id, 'Okey,aqui estaremos esperandote. Cuidate!')
            elif call.data == 'registr':
                bot.send_message(call.message.chat.id, 'vale emprecemos')
                bot.send_message(call.message.chat.id, 'Ponga su primer nombre:')
                @bot.message_handler(content_types=['text'])
                def firststep(message):
                    user_data['name'] = message.text
                    msg = bot.send_message(message.chat.id, 'ingrese su apellido:')
                    bot.register_next_step_handler(msg , secondstep)

    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    idm = message.from_user.id
    dataconnector.make_userActive(idm)
    bot.send_message(message.chat.id, 'Te suscribiste con éxito')


@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    idm = message.from_user.id
    dataconnector.make_userNotActive(idm)
    bot.send_message(message.chat.id, "De repente anulaste la suscripcion")


@bot.message_handler(commands=['start'])
def start_message(message):
    butt1 = types.KeyboardButton('/subscribe')
    butt2 = types.KeyboardButton('/unsubscribe')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=4)
    markup.add(butt1, butt2)
    bot.send_message(message.chat.id, 'Hola!',reply_markup=markup)
    butt_reg = types.InlineKeyboardButton('Registrate',callback_data='registr')
    markup = types.InlineKeyboardMarkup()
    markup.add(butt_reg)
    dataconnector.add_user(message.from_user.username, message.from_user.id, False)
    bot.send_message(message.chat.id, ("¡Bienvenid@ {username}.\n! "
                                       "Soy el Bot asistente de Lifetime Team🤖, en\n"
                                       "donde te guiaremos paso a paso cómo \n"
                                       "dar tus primeros pasos, junto con tu \n"
                                       "patrocinador y con el sistema virtual,\n"
                                       "para ir avanzando mes a mes y alcanzar\n"
                                       "las metas que te propongas en el \n"
                                       "negocio🚀").format(
        username=message.from_user.username), reply_markup=markup)




bot.polling(none_stop=True, interval=0)
