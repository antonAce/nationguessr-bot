import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from fsm import state_storage
from handlers import root_router
from vars import TOKEN

logger = logging.getLogger()
logger.setLevel(logging.INFO)


async def main():
    if not TOKEN:
        logger.error(
            "API Token is empty or invalid. Set it in `BOT_TOKEN` environment variable."
        )
        sys.exit(1)

    bot = Bot(TOKEN, parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher(storage=state_storage)
    dp.include_router(root_router)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
