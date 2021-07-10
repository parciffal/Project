from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

markup = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text='First Plan', callback_data='plan_1')
b2 = InlineKeyboardButton(text='Second Plan', callback_data='plan_2')
markup.add(b1)
markup.add(b2)

markup_plan1 = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text='Buy Plan 1', callback_data='buy_1')
b2 = InlineKeyboardButton(text='<<back', callback_data='back')
markup_plan1.add(b1)
markup_plan1.add(b2)

markup_plan2 = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text='Buy Plan 2', callback_data='buy_2')
b2 = InlineKeyboardButton(text='<<back', callback_data='back')
markup_plan2.add(b1)
markup_plan2.add(b2)