import asyncio
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import router
from bot.db import connect_db, create_users_table

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    conn = await connect_db()
    await create_users_table(conn)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
