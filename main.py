import asyncio, logging, sys
from aiogram import Bot, Dispatcher
from decouple import config
from app.handlers.basic_handlers import router as basic_router 
from app.handlers.todo_handlers import router as todo_router


TOKEN = config('TELEGRAM_TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher()

dp.include_router(basic_router)
dp.include_router(todo_router)


async def main():
    await dp.start_polling(bot)      

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except:
        print('Bot Stopped!')
        
