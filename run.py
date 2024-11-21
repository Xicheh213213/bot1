from aiogram import Bot, Dispatcher
import asyncio
import os
from dotenv import load_dotenv
from app.admin import admin
from app.user import user
from app.database.models import async_main

async def main():
    load_dotenv()
    await async_main()
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(user,admin)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')