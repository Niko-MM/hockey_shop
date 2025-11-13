from aiogram import Dispatcher, Bot
from config import bot_settings
from handlers.client import user
import asyncio
import logging


async def main():
    bot = Bot(bot_settings.bot_token)
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Остановка')
