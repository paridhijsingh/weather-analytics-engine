from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# This creates a local SQLite database file named 'weather.db'
DATABASE_URL = "sqlite:///./weather.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a class called 'WeatherLog' that inherits from 'Base'
class WeatherLog(Base):
    __tablename__ = "weather_logs"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    temperature = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Creates the table in weather.db file
Base.metadata.create_all(bind=engine)