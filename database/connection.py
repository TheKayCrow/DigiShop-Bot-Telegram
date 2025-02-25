from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import Config
from .models import Base

def init_db():
    engine = create_engine(Config.DATABASE_URL)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

SessionLocal = init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()