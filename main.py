from bot_client import bot
from dispatcher import Dispatcher
import asyncio

dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())