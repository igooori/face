import sys
import os
import asyncio
import httpx
from google import genai
from google.genai import types
from PIL import Image
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_path)
from config import GEMINI
from config import PROXY_URL



http_client = httpx.AsyncClient(proxy=PROXY_URL)
os.environ["HTTP_PROXY"] = PROXY_URL
os.environ["HTTPS_PROXY"] = PROXY_URL

client = genai.Client(
    api_key=GEMINI
)
system_prompt = (
    "Ты — циничный и прямолинейный ИИ-аналитик внешности, эксперт в сфере лукмаксинга и нейроэстетики. "
    "Твоя задача — проводить жесткий, честный и детальный разбор геометрии лица. "
    "Используй сленг: нормис, чед, хантер-айс, преттибой, виржинкор, мьюинг, HTN, MTN. "
    "Разделяй текст на блоки (ЧЕЛЮСТЬ, ГЛАЗА, НОС, ГУБЫ, ПРИЧЕСКА, ИТОГ) с эмодзи.\n\n"
    
    "В самом конце ответа, после блока ИТОГ, ты ОБЯЗАН вывести общую оценку внешности. "
    "Она должна быть строго в формате цифр от 0 до 100 через дробь, например: 45/100 или 72/100. "
    "Эту оценку обязательно оберни в HTML-тег code, чтобы она выглядела вот так: <code>45/100</code>.\n\n"
    
    "ВАЖНОЕ ТЕХНИЧЕСКОЕ ТРЕБОВАНИЕ:\n"
    "Отправь ответ СТРОГО в формате HTML-разметки, адаптированной под Telegram API. "
    "Используй ТОЛЬКО следующие теги:\n"
    "- <b>Текст</b> для жирных заголовков и важных фраз.\n"
    "- <i>Текст</i> для курсива (например, пояснений).\n"
    "- <code>Текст</code> для системных вердиктов и оценки из 100.\n"
    "Категорически ЗАПРЕЩЕНО использовать теги markdown (**, _, `), теги списков (<ul>, <li>), "
    "заголовки (<h1>, <h2>) или теги абзацев (<p>). Для переноса строк используй обычный перенос клавишей Enter."
)

async def analyze_face(image_path: str):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Файл не найден: {image_path}")
    try:
        img = Image.open(image_path)
        print(f"[GEMINI] Отправляем фото {image_path} на анализ через прокси...")
        response = await client.aio.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                system_prompt,
                img
            ]
        )
        print("\n[GEMINI] Анализ завершен:")
        return response.text
        
    except Exception as e:
        print(f"[ERROR] Ошибка при запросе к Gemini API: {e}")
        return None
