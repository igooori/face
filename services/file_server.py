from aiogram import Bot
import time
from aiogram.types import PhotoSize
import os

async def save_photo(bot:Bot,photo: PhotoSize,user_id:int) -> str | None:
    try:
        file = await bot.get_file(photo.file_id)
        file_ext = os.path.splitext(file.file_path)[1] if file.file_path else ".jpg"
        timestemp = int(time.time())
        file_name = f"photo_{user_id}_{timestemp}{file_ext}"
        dir_path = "photo"
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path,file_name)
        await bot.download_file(file.file_path, file_path)
        return file_path
    except Exception as e:
        print(f"Ошбика: {e}")
        return None

