from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from ..schemas import RecipeSchema, CreateRecipeSchema
from ..database import get_db
from ..repository.recipe import RecipeRepository
from ..auth.auth_bearer import JWTBearer

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

@router.post("/", response_model=RecipeSchema, dependencies=[Depends(JWTBearer())])
async def create_recipe(
    recipe_data: CreateRecipeSchema, db: Session = Depends(get_db)
):
    created_recipe = RecipeRepository.create_recipe(db, recipe_data)
    return created_recipe