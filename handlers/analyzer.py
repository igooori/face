from aiogram import Router,F,Bot
from aiogram.types import Message
from aiogram.filters import Command
from services.file_server import save_photo
from services.gemini_ai import analyze_face
import os

router = Router()

@router.message(F.photo)
async def photo_face(message:Message, bot:Bot):
    local_path = await save_photo(bot, message.photo[-1], message.from_user.id)
    report = await analyze_face(local_path)
    await message.answer(report, parse_mode='HTML')
    os.remove(local_path)
    
    