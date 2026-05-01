from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
import psycopg2 # type: ignore
from psycopg2.extras import RealDictCursor # type: ignore
import time
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()


    
while True:
    try:
        conn = psycopg2.connect(
            host=settings.database_hostname,
            port=settings.database_port, 
            database=settings.database_name, 
            user=settings.database_username, 
            password=settings.database_password,
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break 
    except Exception as e:
        print(f"Connecting to database failed")
        print(f"Error: {e}")
        time.sleep(2)
