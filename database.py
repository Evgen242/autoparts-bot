from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()


class AutoPart(Base):
    __tablename__ = "autoparts"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    car_brand = Column(String(50))
    car_model = Column(String(50))
    part_number = Column(String(50))
    quantity = Column(Integer, default=0)
    price = Column(Float)
    location = Column(String(100))
    description = Column(String(500))
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<AutoPart {self.name} for {self.car_brand} {self.car_model}>"


# Используем переменную окружения или значение по умолчанию
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://autoparts_user:Moto2025@localhost/autoparts_db"
)
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)
