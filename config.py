import os

from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
env_file = os.path.join(BASE_DIR, '.env')
load_dotenv(env_file)


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')


print(Config.SECRET_KEY)
