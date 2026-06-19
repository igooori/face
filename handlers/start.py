from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.keyboards import get_hello_keyboards

router = Router()

hello_text = """<b>Привет! 👋</b>

Я — ИИ-аналитик внешности. Загрузи своё фото, и я честно разберу твою привлекательность по баллам (0–100) и дам конкретные советы, как стать ещё лучше.

Что я оцениваю:
• Симметрию и пропорции лица
• Гармонию черт (глаза, нос, скулы, челюсть)
• Состояние кожи и визуальный возраст
• Общую "вау-эффект" привлекательность

<b>Правила для лучшего результата:</b>
📸 Анфас или лёгкий ¾
☀️ Хорошее освещение (естественный свет — идеально)
🚫 Без сильных фильтров и макияжа

Пришли мне одну фотографию — и через несколько секунд получишь подробный разбор ✨
"""

@router.message(Command('start'))
async def start(message:Message):
    await message.answer(text=hello_text,reply_markup=get_hello_keyboards(),parse_mode='HTML')