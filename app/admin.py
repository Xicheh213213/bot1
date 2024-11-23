from aiogram import Router,F
from aiogram.filters import Filter,Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

admin = Router()

admins = [5346148011]

class AdminProtect(Filter):
    def __init__(self):
        self.admin = admins
    async def __call__(self,message:Message):
        return message.from_user.id in self.admin

@admin.message(AdminProtect(),Command('apanel'))
async def a_panel(message:Message):
    await message.answer('This panel of admin')