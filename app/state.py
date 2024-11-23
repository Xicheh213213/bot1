from aiogram.fsm.state import State, StatesGroup

class NewLetters(StatesGroup):
    message = State()
    photo = State()

class Itemname(StatesGroup):
    itemname = State()