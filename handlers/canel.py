from aiogram.types import Message
from aiogram import Router,F
from aiogram.types import CallbackQuery
from keyboards.keyboards import get_hello_keyboards
router = Router()
hello_text = """<b>Привет! 🤖 На связи ИИ-сканер внешности.</b>

Я умею раскладывать геометрию лица на четкие метрики и проводить тест привлекательности <b>от 0 до 100 баллов</b>. Загрузи качественное фото, и я сделаю для тебя персональную карточку:

• <b>Форма лица и симметрия</b> в процентах
• <b>Гармония черт</b> и оценка привлекательности
• <b>Состояние кожи</b> и твой визуальный возраст

👇 <b>Пришли мне одну фотографию лица</b> (анфас, при хорошем освещении, без фильтров), и через 10 секунд забирай результат!"""

@router.callback_query(F.data == 'canel')
async def canel(callback:CallbackQuery):
    try:
        await callback.message.edit_text(text=hello_text,parse_mode='HTML', reply_markup=get_hello_keyboards())
    except:
        await callback.message.answer(text=hello_text,parse_mode='HTML', reply_markup=get_hello_keyboards())
    await callback.answer()


