from typing import List
from pydantic import BaseModel


class ShowFavouriteRecipe(BaseModel):
    id: int
    recipe_image: str
    ingredients: str
    procedure: str
    number_of_people_served: int
    time_in_minutes: int
    country: str

    class Config:
        orm_mode = True


class ShowUserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    profile_photo: str
    country: str
    phone_number: str
    favourite_recepes: List[ShowFavouriteRecipe]

    class Config:
        orm_mode = True


class ShowCommentSchema(BaseModel):
    id: int
    comment: str

    class Config:
        orm_mode = True


class RecipeSchema(BaseModel):
    id: int
    recipe_image: str
    ingredients: str
    procedure: str
    number_of_people_served: int
    time_in_minutes: int
    country: str
    rating: float
    user: ShowUserSchema
    comments: List[ShowCommentSchema]

    class Config:
        orm_mode = True


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    profile_photo: str
    country: str
    phone_number: str
    password: str
