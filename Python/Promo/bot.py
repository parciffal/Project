from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from stateed import Adding,Edit,Delete
import config
from aiogram.dispatcher import FSMContext
# database imports
from database import DataConnector
import keyboards
import logging

storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)
db = DataConnector()
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,)


@dp.message_handler(state=Adding.S0)
async def promo_name(message: types.Message, state: FSMContext):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await state.update_data(name=message.text)
    await bot.send_message(message.chat.id, 'What is the promotion?')

    await Adding.next()


@dp.message_handler(state=Adding.S1)
async def promo_promo(message: types.Message, state: FSMContext):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await state.update_data(promo=message.text)
    await bot.send_message(message.chat.id, 'Any expiry for promo code?')
    await Adding.next()


@dp.message_handler(state=Adding.S2)
async def promo_exipre(message: types.Message, state: FSMContext):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await state.update_data(expire=message.text)
    await bot.send_message(message.chat.id, 'Any Terms and Condition?')
    await Adding.next()


@dp.message_handler(state=Adding.S3)
async def promo_terms(message: types.Message, state: FSMContext):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await state.update_data(terms=message.text)
    await bot.send_message(message.chat.id, 'Any limited quantity?')
    await Adding.next()


@dp.message_handler(state=Adding.S4)
async def promo_quantity(message: types.Message, state: FSMContext):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await state.update_data(limit=message.text)
    await bot.send_message(message.chat.id, 'How many hours do you want to display the promo code in the group?')
    await Adding.next()


@dp.message_handler(state=Adding.S5)
async def promo_hour(message: types.Message, state: FSMContext):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await state.update_data(time=message.text)
    await bot.send_message(message.chat.id, 'What is promo code?')
    await Adding.next()


@dp.message_handler(state=Adding.S6)
async def promo_hour(message: types.Message, state: FSMContext):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await state.update_data(code=message.text)
    data = await state.get_data()
    answer1 = data.get("name")
    db.add_user(message_id=message.message_id,
                name=data.get("name"),
                promo=data.get("promo"),
                expire=data.get("expire"),
                terms=data.get("terms"),
                limit=data.get("limit"),
                time=data.get("time"),
                code=data.get("code"))
    await bot.send_message(message.chat.id, 'Promo code '+str(answer1)+' saved')
    await state.finish()


@dp.message_handler(state=Edit.S0)
async def edit_one(message: types.Message, state: FSMContext):
    try:
        if message.text.isalnum():
            ids = db.get_ids()
            expd = False
            for i in ids:
                if int(message.text) == int(i):
                    expd = True
                else:
                    pass
            if expd:
                state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
                await state.update_data(id=message.text)
                await bot.send_message(chat_id=message.chat.id,
                                       text='Choose from keyboard to edit',
                                       reply_markup=keyboards.markup_edit)
                Edit.S1.set()
            else:
                await bot.edit_message_text(message_id=message.message_id,
                                            chat_id=message.chat.id,
                                            text='Wrong id try again')
                await Edit.S0.set()
        else:
            await bot.edit_message_text('Wrong id try again')
            await Edit.S0.set()
    except Exception as e:
        print(repr(e))


@dp.message_handler(state=Delete.S0)
async def delete(message: types.Message, state: FSMContext):
    try:
        if message.text.isalnum():
            ids = db.get_ids()
            expd = False
            for i in ids:
                if int(message.text) == int(i):
                    expd = True
                else:
                    pass
            if expd:
                db.remove(int(message.text))
                await bot.send_message(chat_id=message.chat.id,
                                       text='Message deleted\nChoose from keyboard ',
                                       reply_markup=keyboards.markup_start)
                await state.finish()
            else:
                await bot.edit_message_text(message_id=message.message_id,
                                            chat_id=message.chat.id,
                                            text='Wrong id try again')
                await Delete.S0.set()
        else:
            await bot.edit_message_text('Wrong id try again')
            await Delete.S0.set()
    except Exception as e:
        print(repr(e))


@dp.message_handler(state=Edit.S2)
async def edit_name(message: types.Message, state: FSMContext):
    try:
        state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
        data = await state.get_data()
        answer_id = data.get("id")
        db.change_name(answer_id, message.text)
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Name changed',
                                    reply_markup=keyboards.markup_start)
        await state.finish()
    except Exception as e:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Something wrong try again')
        await Edit.S2.set()


@dp.message_handler(state=Edit.S3)
async def edit_promo(message: types.Message, state: FSMContext):
    try:
        state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
        data = await state.get_data()
        answer_id = data.get("id")
        db.change_promo(answer_id, message.text)
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Name changed',
                                    reply_markup=keyboards.markup_start)
        await state.finish()
    except Exception as e:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Something wrong try again')
        await Edit.S3.set()


@dp.message_handler(state=Edit.S4)
async def edit_expire(message: types.Message, state: FSMContext):
    try:
        state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
        data = await state.get_data()
        answer_id = data.get("id")
        db.change_expire(answer_id, message.text)
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Name changed',
                                    reply_markup=keyboards.markup_start)
        await state.finish()
    except Exception as e:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Something wrong try again')
        await Edit.S4.set()


@dp.message_handler(state=Edit.S5)
async def edit_terms(message: types.Message, state: FSMContext):
    try:
        state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
        data = await state.get_data()
        answer_id = data.get("id")
        db.change_terms(answer_id, message.text)
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Name changed',
                                    reply_markup=keyboards.markup_start)
        await state.finish()
    except Exception as e:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Something wrong try again')
        await Edit.S5.set()


@dp.message_handler(state=Edit.S6)
async def edit_limit(message: types.Message, state: FSMContext):
    try:
        state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
        data = await state.get_data()
        answer_id = data.get("id")
        db.change_limit(answer_id, message.text)
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Limit changed',
                                    reply_markup=keyboards.markup_start)
        await state.finish()
    except Exception as e:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Something wrong try again')
        await Edit.S6.set()


@dp.message_handler(state=Edit.S7)
async def edit_time(message: types.Message, state: FSMContext):
    try:
        state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
        data = await state.get_data()
        answer_id = data.get("id")
        db.change_time(answer_id, message.text)
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Time changed',
                                    reply_markup=keyboards.markup_start)
        await state.finish()
    except Exception as e:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Something wrong try again')
        await Edit.S7.set()


@dp.message_handler(state=Edit.S8)
async def edit_code(message: types.Message, state: FSMContext):
    try:
        state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
        data = await state.get_data()
        answer_id = data.get("id")
        db.change_code(answer_id, message.text)
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Code changed',
                                    reply_markup=keyboards.markup_start)
        await state.finish()
    except Exception as e:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message.message_id,
                                    text='Something wrong try again')
        await Edit.S8.set()


@dp.callback_query_handler(lambda call: call.data in ['ch_name', 'ch_promo', 'ch_expire', 'ch_terms', 'ch_limit', 'ch_time', 'ch_code', 'back'], state=Edit.S1)
async def call_edit(call: types.CallbackQuery, state: FSMContext):
    try:
        if call.data == 'ch_name':
            await bot.edit_message_text('Send Name to change',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
            await Edit.S2.set()
        elif call.data == 'ch_promo':
            await bot.edit_message_text('Send Promo to change',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
            await Edit.S3.set()
        elif call.data == 'ch_expire':
            await bot.edit_message_text('Send Expire to change',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
            await Edit.S4.set()
        elif call.data == 'ch_terms':
            await bot.edit_message_text('Send Terms to change',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
            await Edit.S5.set()
        elif call.data == 'ch_limit':
            await bot.edit_message_text('Send Limit to change',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
            await Edit.S6.set()
        elif call.data == 'ch_time':
            await bot.edit_message_text('Send Time to change',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
            await Edit.S7.set()
        elif call.data == 'ch_code':
            await bot.edit_message_text('Send Code to change',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
            await Edit.S8.set()
    except Exception as e:
        print(repr(e))


@dp.callback_query_handler(lambda call: call.data in ['new_promo', 'show', 'edit', 'delete', 'send', 'export'])
async def call_start(call: types.CallbackQuery):
    try:
        if call.data == 'new_promo':
            await bot.send_message(call.message.chat.id, 'What is the name of the promo')
            await Adding.S0.set()
        elif call.data == 'edit':
            await bot.send_message(call.message.chat.id, 'Send id of message to edit')
            await Edit.S0.set()
        elif call.data == 'delete':
            await bot.send_message(call.message.chat.id, 'Send id of message to delete')
            await Delete.S0.set()
        elif call.data == 'send':
            pass
        elif call.data == 'export':
            pass
        elif call.data == 'show':
            await bot.send_message(call.message.chat.id, text='Your Promos')
            promos = db.get_all_ids()
            for promo in promos:
                await bot.send_message(call.message.chat.id,
                                       text='Promo id: ' + str(promo.get('message_id')) + '\n'
                                                                                          'name: ' + promo.get(
                                           'name') + '\n'
                                                     'promo: ' + promo.get('promo') + '\n'
                                                                                      'expire: ' + promo.get(
                                           'expire') + '\n'
                                                       'terms: ' + promo.get('terms') + '\n'
                                                                                        'limit: ' + promo.get(
                                           'limit') + '\n'
                                                      'time: ' + promo.get('time') + '\n'
                                                                                     'code: ' + promo.get(
                                           'code') + '\n')
    except Exception as e:
        print(repr(e))


@dp.message_handler(commands='start')
async def start(message: types.Message):
    markup = keyboards.markup_start
    await message.answer('Hi choose from keyboard', reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp)
