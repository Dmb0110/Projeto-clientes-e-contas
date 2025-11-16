import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    DATABASE_URL: str = os.getenv('DATABASE_URL')

    #if not DATABASE_URL:
     #   DATABASE_URL = 'postgresql://postgres:davi9090@localhost:5432/banco_teste12_1'

settings = Settings()
