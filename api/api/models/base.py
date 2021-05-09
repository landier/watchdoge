import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

if os.getenv('ENV') == 'PROD':
    SQLALCHEMY_DATABASE_URL = "sqlite:////data/watchdodge.db"
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./watchdodge.db"

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},
    echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = sqlalchemy.MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
