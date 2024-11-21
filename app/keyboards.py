from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton,InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder

from app.database.requests import get_categories, get_subcategory, get_items

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог'),
                                     KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Поиск товара'),
                                     KeyboardButton(text='Контакты')]],
                                     resize_keyboard= True)

async def item_buttons(item_id):
    keyboard = item_buttons = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='В корзину',callback_data=f'basket_{item_id}')],
                                                        [InlineKeyboardButton(text='Назад',callback_data='back')]])
    return keyboard

async def catalor():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name,callback_data=f'category_{category.id}'))
    return keyboard.adjust(2).as_markup()

async def subcategory(categor_id):
    all_subcategory = await get_subcategory(categor_id)
    keyboard = InlineKeyboardBuilder()
    for subcategory in all_subcategory:
        keyboard.add(InlineKeyboardButton(text=subcategory.name,callback_data=f'subcategory_{subcategory.id}'))
    return keyboard.adjust(2).as_markup()

async def items(subcategory_id):
    all_items = await get_items(subcategory_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name,callback_data=f'item_{item.id}'))
    return keyboard.adjust(2).as_markup()