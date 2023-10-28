from sqlalchemy.orm import relationship, validates
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
    updated_at = Column(DateTime, onupdate=func.now())

    favourite_recepes = relationship(
        "Recipe", secondary="favourites", back_populates="user_favourites"
    )

    recipes = relationship("Recipe", backref="user", cascade="all, delete")


class Recipe(BaseModel):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    recipe_image = Column(String, nullable=False)
    ingredients = Column(String)
    procedure = Column(String)
    number_of_people_served = Column(Integer, nullable=False)
    time_in_minutes = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    comments = relationship("Comment", backref="recipe", cascade="all, delete")
    ratings = relationship("Rating", backref="recipe", cascade="all, delete")
    user_favourites = relationship(
        "User", secondary="favourites", back_populates="favourite_recepes"
    )

    @property
    def rating(self):
        length = len(self.ratings)
        if length == 0:
            return 0
        total = sum([r.rating for r in self.ratings])

        return total / length


class Comment(BaseModel):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    comment = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class Favourite(BaseModel):
    __tablename__ = "favourites"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class Rating(BaseModel):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    created_at = Column(DateTime, server_default=func.now())
    created_at = Column(DateTime, onupdate=func.now())

    @validates("rating")
    def validate_rating(self, key, rating):
        if not isinstance(rating, int):
            raise ValueError("Rating must be a number")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be in range 1-5")
        return rating
