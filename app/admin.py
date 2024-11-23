from aiogram import Router,F
from aiogram.filters import Filter,Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.state import NewLetters
from app.database.requests import get_users
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

@admin.message(Command('newl'))
async def cmd_newl(message:Message,state:FSMContext):
    await state.set_state(NewLetters.message)
    await message.answer('Type a message')

@admin.message(NewLetters.message)
async def type_message(message:Message,state:FSMContext):
    await state.update_data(message = message.text)
    await state.set_state(NewLetters.photo)
    await message.answer('Send a photo')

@admin.message(NewLetters.photo, F.photo)
async def send_photo(message:Message,state:FSMContext):
    await state.update_data(photo = message.photo[-1].file_id)
    data = await state.get_data()
    users = await get_users()
    for user in users:
        try:
            await message.bot.send_photo(chat_id=user.tg_id, photo=data['photo'],caption=data['message'])
        except Exception as e:
            print('')
    await state.clear()
