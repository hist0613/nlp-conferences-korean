import os
from dotenv import load_dotenv

load_dotenv()

MAX_NB_SHOW = 20
MAX_NB_GPT3_ATTEMPT = 3
TIME_PAUSE_SEC = 15

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
