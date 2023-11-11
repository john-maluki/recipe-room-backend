from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./server/recipe_room.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/recipe-room"
SQLALCHEMY_DATABASE_URL = "postgresql://john_maluki_postgres_user:A0Is8nZ6Qqxlgd0hudgRqS6R5ngBExtN@dpg-cl7ppmqvokcc73aos0ng-a.oregon-postgres.render.com/john_maluki_postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class BaseModel(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
