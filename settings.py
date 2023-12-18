import os
from dotenv import load_dotenv

load_dotenv()

MAX_NB_SHOW = 100
MAX_NB_GPT3_ATTEMPT = 3

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
