import asyncio
from aiogram import Bot,Dispatcher
from config import TOKEN
from aiogram.types import BotCommand
from handlers.start import router as start_router
from handlers.main_menu import router as main_router
from handlers.canel import router as canel_router

dp = Dispatcher()

async def set_my_commands(bot:Bot):
    commands = [
        BotCommand(command='start', description='Запуск бота')
    ]
    await bot.set_my_commands(commands)

async def main():
    bot = Bot(
        token=TOKEN
    )
    dp.include_router(start_router)
    dp.include_router(main_router)
    dp.include_router(canel_router)
    print('Бот запускаеться')
    await set_my_commands(bot)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')