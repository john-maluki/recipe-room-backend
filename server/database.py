from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./server/recepe_room.db")
SessionLocal = sessionmaker(bind=engine)


class BaseModel(DeclarativeBase):
    pass
