from sqlalchemy.orm import Session
from typing import List, Union
from fastapi import APIRouter, Depends, status, HTTPException

from ..schemas import RecipeSchema, CreateRecipeSchema, UpdateRecipeSchema
from ..database import get_db
from ..repository.recipe import RecipeRepository
from ..repository.user import UserRepository
from ..auth.auth_bearer import JWTBearer
from .favourite_recipes import get_user_id
from ..models import User

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/", response_model=List[RecipeSchema])
async def get_recipes(db: Session = Depends(get_db)):
    return RecipeRepository.get_all(db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=RecipeSchema,
    dependencies=[Depends(JWTBearer())],
)
async def get_recipe_by_id(id: int, db: Session = Depends(get_db)):
    recipe = RecipeRepository.get_recipe_by_id(id, db)
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!"
        )
    return recipe

@router.get("/user/{user_id}", response_model=List[RecipeSchema], dependencies=[Depends(JWTBearer())])
async def get_recipes_by_user(user_id: int, db: Session = Depends(get_db)):
    recipes = RecipeRepository.get_recipes_by_user(user_id, db)
    return recipes

@router.post("/", response_model=RecipeSchema, dependencies=[Depends(JWTBearer())])
async def create_recipe(
    recipe_data: CreateRecipeSchema, db: Session = Depends(get_db)
):
    created_recipe = RecipeRepository.create_recipe(db, recipe_data)
    return created_recipe

@router.put("/{id}", response_model=RecipeSchema, dependencies=[Depends(JWTBearer())])
async def update_recipe(id: int, recipe_data: UpdateRecipeSchema, db: Session = Depends(get_db)):
    existing_recipe = RecipeRepository.get_recipe_by_id(id, db)
    if not existing_recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!"
        )
    
    updated_recipe = RecipeRepository.update_recipe(db, existing_recipe, recipe_data)
    return updated_recipe

@router.delete("/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: int, current_user: Union[int, User] = Depends(get_user_id), db: Session = Depends(get_db)):
        if isinstance(current_user, int):
            current_user = UserRepository.get_user_by_id(current_user, db)

        recipe = RecipeRepository.get_recipe_by_id(recipe_id, db)

        if not recipe:
            raise HTTPException(status_code=404, detail="Recipe not found")

        if recipe.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="You are not allowed to delete this recipe")

        RecipeRepository.delete_recipe(recipe_id, db)
        return {"message": "Recipe deleted successfully"}
    