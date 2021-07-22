from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from stateed import Adding
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


@dp.message_handler(commands='NewPromo', state=None)
async def new_promo(message : types.Message):
    await bot.send_message(message.chat.id, 'What is the name of the promo')
    await Adding.S0.set()


@dp.message_handler(commands='Show')
async def show(message: types.Message):
    await bot.send_message(message.chat.id, text='Your Promos')
    promos = db.get_all_ids()
    for promo in promos:
        await bot.send_message(message.chat.id,
                               text='Promo id: '+str(promo.get('message_id'))+'\n'
                                    'name: '+promo.get('name')+'\n'
                                    'promo: '+promo.get('promo')+'\n'
                                    'expire: '+promo.get('expire')+'\n'
                                    'terms: '+promo.get('terms')+'\n'
                                    'limit: '+promo.get('limit')+'\n'
                                    'time: '+promo.get('time')+'\n'
                                    'code: '+promo.get('code')+'\n')
if __name__ == '__main__':
    executor.start_polling(dp)
