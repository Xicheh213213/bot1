from aiogram import Router,F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart,Command
from app import keyboards as kb
from app.database import requests as rq

user = Router()

@user.message(CommandStart())
async def cmd_start(message:Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Привет, я твой робот помощник',
                         reply_markup=kb.main)
    
@user.message(F.text == 'Каталог')
async def catalog(message:Message):
    await message.answer('Выберите категорию товара',reply_markup= await kb.catalor())

@user.callback_query(F.data.startswith('category_'))
async def category_subcategory(callback:CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите подкатегорю',reply_markup= await kb.subcategory(callback.data.split('_')[1]))


@user.callback_query(F.data.startswith('subcategory_'))
async def category_subcategory(callback:CallbackQuery):
    await callback.answer('Вы выбрали подкатегорию')
    await callback.message.answer('Выберите товар',reply_markup= await kb.items(callback.data.split('_')[1]))

@user.callback_query(F.data.startswith('item_'))
async def category_subcategory(callback:CallbackQuery):
    item = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.edit_text(f'Название: {item.name}\nОписание: {item.descripion}\nЦена: {item.price}',reply_markup= await kb.item_buttons(callback.data.split('_')[1]))