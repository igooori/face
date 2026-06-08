from aiogram.types import InlineKeyboardMarkup
from .bilder import get_callback_btns

def get_hello_keyboards() -> InlineKeyboardMarkup:
    return get_callback_btns(
        btns= {
            "⚙️ Как это работает?": "works",
            "📸 Примеры результатов": "example"
        },
        sizes=(2,),
    )