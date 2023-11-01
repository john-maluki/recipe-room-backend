from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from ..schemas import  FavouriteRecipe
from ..auth.auth_bearer import JWTBearer
from ..database import get_db
from ..repository.recipe import RecipeRepository
from ..repository.favourite_recipe import FavouriteRecipeRepository



router = APIRouter(prefix="/favourite_recipes", tags=["favourite_recipes"])

@router.post("/favourite", response_model=FavouriteRecipe, dependencies=[Depends(JWTBearer())])
async def create_favourite_recipe(
    recipe_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):

    if not RecipeRepository.get_recipe_by_id(recipe_id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    existing_favourite = FavouriteRecipeRepository.get_favourite_recipe_by_user_and_recipe(user_id, recipe_id, db)
    if existing_favourite:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Recipe already marked as favourite",
        )

    new_favourite_recipe = FavouriteRecipeRepository.create_favourite_recipe(db, user_id=user_id, recipe_id=recipe_id)
    return new_favourite_recipe

@router.get("/favourite_recipes/{user_id}", response_model=List[FavouriteRecipe])
async def get_favourites_by_user(user_id: int, db: Session = Depends(get_db)):

    favourites = FavouriteRecipeRepository.get_favourite_recipes_by_user(db, user_id)
    return favourites

@router.get("/all", response_model=List[FavouriteRecipe])
async def get_all_favourite_recipes(db: Session = Depends(get_db)):
    all_favourites = FavouriteRecipeRepository.get_all_favourite_recipes(db)
    return all_favourites