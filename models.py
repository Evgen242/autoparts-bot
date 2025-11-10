from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
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
