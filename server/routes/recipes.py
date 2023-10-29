from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from ..schemas import RecipeSchema
from ..models import Recipe
from ..database import get_db

router = APIRouter()


@router.get("/recipes", response_model=List[RecipeSchema], tags=["recipes"])
async def get_recipes(db: Session = Depends(get_db)):
    recipes = db.query(Recipe).all()
    return recipes


@router.get(
    "/recipes/{id}",
    status_code=status.HTTP_200_OK,
    response_model=RecipeSchema,
    tags=["recipes"],
)
async def get_recipe_by_id(id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter_by(id=id).first()
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!"
        )
    return recipe
