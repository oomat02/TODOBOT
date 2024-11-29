from aiogram import types, Router, F
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Dobro pojalovat TODO BOT!')

#TODO - написать оброботчик/ help - Отпровляет два сообщение : 1."Инструкция по использованию бота", 2.Инструкция