from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String, Date, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_USERNAME = os.getenv("NEWUSERNAME")
DB_PASSWORD = os.getenv("PASSWORD")
DB_HOST = os.getenv("HOST")
DB_DATABASE = os.getenv("DATABASE")

engine = create_engine(f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}", connect_args={
        "ssl":{
            'ssl_ca': '/etc/ssl/certs/ca-certificates.crt',
        }
})

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(100))
    user_email = Column(String(100))
    user_password = Column(String(100))
    user_status = Column(Integer)

class Event(Base):
    __tablename__ = "event"
    event_id = Column(Integer, primary_key=True, autoincrement=True)
    event_title = Column(String(100))
    event_description = Column(String(100))
    event_date = Column(Date)
    user_id = Column(Integer)

Session = sessionmaker(bind=engine)

