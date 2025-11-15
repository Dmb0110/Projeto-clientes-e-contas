#import os
#from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from app.core.config import settings

#load_dotenv()
#DATABASE_URL = os.getenv('DATABASE_URL')
#DATABASE_URL = 'postgresql://postgres:davi9090@localhost:5432/banco_teste12_1'

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
