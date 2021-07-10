from aiogram.dispatcher.filters.state import State, StatesGroup


class First(StatesGroup):
    S1 = State()
    S2 = State()
    S3 = State()
    S4 = State()


class Second(StatesGroup):
    R1 = State()
    R2 = State()
    R3 = State()
    R4 = State()
