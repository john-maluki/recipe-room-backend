from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from ..schemas import RecipeSchema
from ..database import get_db
from ..repository.recipe import RecipeRepository

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("/", response_model=List[RecipeSchema])
async def get_recipes(db: Session = Depends(get_db)):
    return RecipeRepository.get_all(db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=RecipeSchema,
)
async def get_recipe_by_id(id: int, db: Session = Depends(get_db)):
    recipe = RecipeRepository.get_recipe_by_id(id, db)
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!"
        )
    return recipe
