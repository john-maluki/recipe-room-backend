from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from ..schemas import  FavouriteRecipe
from ..auth.auth_bearer import JWTBearer, decodeJWT
from ..database import get_db
from ..repository.recipe import RecipeRepository
from ..repository.favourite_recipe import FavouriteRecipeRepository



router = APIRouter(prefix="/favourite_recipes", tags=["favourite_recipes"])

def get_user_id(token: str = Depends(JWTBearer())) -> int:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decodeJWT(token)
        user_id = payload["sub"]["id"] 
        return user_id
    except Exception as e:
        raise credentials_exception from e


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

@router.get("/{user_id}", response_model=List[FavouriteRecipe])
async def get_favourites_by_user(user_id: int, db: Session = Depends(get_db)):

    favourites = FavouriteRecipeRepository.get_favourite_recipes_by_user(db, user_id)
    return favourites

@router.get("/all", response_model=List[FavouriteRecipe])
async def get_all_favourite_recipes(db: Session = Depends(get_db)):
    all_favourites = FavouriteRecipeRepository.get_all_favourite_recipes(db)
    return all_favourites

@router.get("/{favourite_id}", response_model=FavouriteRecipe, dependencies=[Depends(JWTBearer())])
async def get_favourite_recipe_by_id(favourite_id: int, db: Session = Depends(get_db)):
    print("Received request for favourite recipe with ID:", favourite_id)

    favourite_recipe = FavouriteRecipeRepository.get_favourite_recipe_by_id(db, favourite_id)
    return favourite_recipe

@router.delete("/{favourite_id}", response_model=dict, dependencies=[Depends(JWTBearer())])
async def delete_favourite_recipe(favourite_id: int, user_id: int = Depends(get_user_id), db: Session = Depends(get_db)):
    existing_favourite = FavouriteRecipeRepository.get_favourite_recipe_by_id(db, favourite_id)

    if not existing_favourite:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )
    
    if str(existing_favourite.user_id).strip() != str(user_id).strip():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own favourite recipes",
        )

    FavouriteRecipeRepository.delete_favourite_recipe(db, favourite_id)

    return {"message": "Recipe deleted successfully"}