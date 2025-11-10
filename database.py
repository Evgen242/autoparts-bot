import os
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Text,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class AutoPart(Base):
    __tablename__ = "autoparts"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    car_brand = Column(String(50), nullable=False)
    car_model = Column(String(50), nullable=False)
    part_number = Column(String(50), nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0.0)
    location = Column(String(100))
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.now)


# Берём готовую строку подключения из .env
DATABASE_URL = os.getenv("DATABASE_URL")

Session = None


def init_db():
    try:
        engine = create_engine(DATABASE_URL)
        global Session
        Session = sessionmaker(bind=engine)

        # создаём таблицы, если их нет
        Base.metadata.create_all(engine)
        print("✅ Подключение к базе успешно")

        # тестовый запрос
        session = Session()
        count = session.execute(text("SELECT COUNT(*) FROM autoparts")).scalar()
        print(f"📦 Запчастей в базе: {count}")
        session.close()

    except Exception as e:
        print(f"❌ Ошибка подключения к базе: {e}")
