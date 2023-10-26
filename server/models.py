from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from server.database import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    profile_photo = Column(String, nullable=False)
    country = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, onupdate=func.now())
