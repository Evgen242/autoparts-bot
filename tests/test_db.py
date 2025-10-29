import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("Подключение успешно! Версия PostgreSQL:", result.scalar())
except Exception as e:
    print("Ошибка подключения:", e)
