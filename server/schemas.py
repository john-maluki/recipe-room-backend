from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class FavouriteRecipe(BaseModel):
    id: int
    recipe_id: int
    user_id: int

    class Config:
        from_attributes = True


class ShowFavouriteRecipe(BaseModel):
    id: int
    recipe_image: str
    ingredients: str
    procedure: str
    number_of_people_served: int
    time_in_minutes: int
    country: str

    class Config:
        from_attributes = True


class ShowUserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    profile_photo: str
    country: str
    phone_number: str
    favourite_recepes: List[ShowFavouriteRecipe] = []

    class Config:
        from_attributes = True


class ShowCommentSchema(BaseModel):
    id: int
    comment: str
    created_at: datetime
    user: ShowUserSchema

    class Config:
        from_attributes = True


class CreateRecipeSchema(BaseModel):
    name: str
    recipe_image: str
    ingredients: str
    procedure: str
    number_of_people_served: int
    time_in_minutes: int
    country: str
    user_id: int

    class Config:
        from_attributes = True


class RecipeSchema(BaseModel):
    id: int
    name: str
    recipe_image: str
    ingredients: str
    procedure: str
    number_of_people_served: int
    time_in_minutes: int
    country: str
    created_at: datetime
    rating: int
    rate_count: int
    favourites: int
    user: ShowUserSchema
    comments: List[ShowCommentSchema]

    class Config:
        from_attributes = True


class UpdateRecipeSchema(BaseModel):
    name: Optional[str]
    recipe_image: Optional[str]
    ingredients: Optional[str]
    procedure: Optional[str]
    number_of_people_served: Optional[int]
    time_in_minutes: Optional[int]
    country: Optional[str]

    class Config:
        from_attributes = True


class CreateUserSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    profile_photo: str
    country: str
    phone_number: str
    password: str


class UpdateUserSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    email: Optional[str]
    profile_photo: Optional[str]
    country: Optional[str]
    phone_number: Optional[str]

    class Config:
        from_attributes = True


class CreateRatingSchema(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    user_id: int
    recipe_id: int


class ShowRatingSchema(BaseModel):
    id: int
    rating: int
    user_id: int
    recipe_id: int

    class Config:
        from_attributes = True


class UpdateRatingSchema(BaseModel):
    rating: int
    user_id: int


class ShowUpdatedRatingSchema(BaseModel):
    id: int
    rating: int
    user_id: int
    recipe_id: int

    class Config:
        from_attributes = True


class LoginSchema(BaseModel):
    email: str
    password: str


class CreateFavouriteSchema(BaseModel):
    user_id: int
    recipe_id: int


class CreateCommentSchema(BaseModel):
    recipe_id: int
    comment: str
    user_id: int
