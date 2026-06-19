from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN=getenv('TOKEN')
GEMINI=getenv('GEMINI')
PROXY_URL=getenv(PROXY_URL)