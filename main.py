import asyncio
import asyncpg
from aiogram import Bot, Dispatcher, Router
from core.Settings import settings
from core.handlers import basic, volunteerHandlers, adminHandlers
from core.middlewares.db import DbSession
import logging


async def start():
    dp = Dispatcher()
    bot = Bot(token=settings.bots.bot_token)
    bot.parse_mode = 'HTML'
    try:
        dp.include_router(basic.router)
        dp.include_router(adminHandlers.router)
        dp.include_router(volunteerHandlers.router)
        pool_connect = await asyncpg.create_pool(user='postgres', password='IKfsvJGKGPofJfuUSOHyUaeXCNcATpYh',
                                                 database='railway', host="monorail.proxy.rlwy.net", port=37016, command_timeout=60)
        dp.update.middleware.register(DbSession(pool_connect))
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    asyncio.run(start())
