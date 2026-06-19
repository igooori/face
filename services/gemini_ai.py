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

PROXY_URL = "http://96ktke:hB8Ey8@45.155.203.44:8000"


http_client = httpx.AsyncClient(proxy=PROXY_URL)
os.environ["HTTP_PROXY"] = PROXY_URL
os.environ["HTTPS_PROXY"] = PROXY_URL

client = genai.Client(
    api_key=GEMINI
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
                "Ты — профессиональный ИИ-аналитик внешности. Проанализируй геометрию лица на фото: "
                "оцени симметрию, форму лица, пропорции и дай краткий, честный и структурированный бэкендерский вердикт.",
                img
            ]
        )
        print("\n[GEMINI] Анализ завершен:")
        return response.text
        
    except Exception as e:
        print(f"[ERROR] Ошибка при запросе к Gemini API: {e}")
        return None
