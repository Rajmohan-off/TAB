from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class SensorReading(Base):
    __tablename__ = 'sensor_readings'
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    voltage_primary = Column(Float)
    voltage_secondary = Column(Float)
    current_primary = Column(Float)
    current_secondary = Column(Float)

def get_engine(db_url='sqlite:///tab_data.db'):
    return create_engine(db_url, echo=False, future=True)

def get_session(engine):
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    return SessionLocal()

def init_db(engine):
    Base.metadata.create_all(engine)
