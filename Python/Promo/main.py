from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from stateed import Adding
import config
from aiogram.dispatcher import FSMContext
# database imports
from database import DataConnector
import keyboard
import logging

storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,)


@dp.message_handler(commands='NewPromo', state=None)
async def start(message : types.Message):
    await bot.send_message(message.chat.id, 'What is the name of the promo')
    await Adding.S0.set()


if __name__ == '__main__':
    executor.start_polling(dp)
