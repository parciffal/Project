from aiogram import types, executor, Dispatcher, Bot
from db import DataConn
import config
from bot_stages import First, Second
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import keyboards

storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
db = DataConn()




@dp.callback_query_handler(lambda call: call.data in ['plan_1', 'plan_2'])
async def call_back_plan(call: types.CallbackQuery):
    try:
        if call.data == 'plan_1':
            await bot.edit_message_text(
                message_id=call.message.message_id,
                chat_id=call.message.chat.id,
                text='Plan for 7 days 20$',
                reply_markup=keyboards.markup_plan1)
            await First.S1.set()
        elif call.data == 'plan_2':
            await bot.edit_message_text(
                message_id=call.message.message_id,
                chat_id=call.message.chat.id,
                text='Plan for 1 mouth 50$',
                reply_markup=keyboards.markup_plan2)
        elif call.data == 'back':
            await bot.edit_message_text(
                                        message_id=call.message.message_id,
                                        chat_id=call.message.chat.id,
                                        text='Hello dear user to buy plan \n choose one from below',
                                        reply_markup=keyboards.markup)
    except Exception as e:
        print(repr(e))

@dp.message_handler(commands='start')
async def start(message: types.Message):
    try:
        print(message)
        db.add_user(message.from_user.id, message.from_user.username)
        await bot.send_message(chat_id=message.chat.id,
                               text='Hello dear user to buy plan \n choose one from below',
                               reply_markup=keyboards.markup)
    except Exception as e:
        print(repr(e))

if __name__ == '__main__':
    executor.start_polling(dp)


