from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from ..schemas import CreateRatingSchema, ShowRatingSchema
from ..repository.rating import RatingRepository
from ..database import get_db
from ..auth.auth_bearer import JWTBearer



router = APIRouter(prefix="/ratings", tags=["ratings"])

@router.post("/", response_model=ShowRatingSchema, status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer())])
async def create_rating(rating_data: CreateRatingSchema, db: Session = Depends(get_db)):
    new_rating = RatingRepository.create_rating(db, rating_data)
    
    return new_rating

@router.get("/{recipe_id}", response_model=List[ShowRatingSchema], dependencies=[Depends(JWTBearer())])
async def get_ratings_by_recipe_id(recipe_id: int, db: Session = Depends(get_db)):
    ratings = RatingRepository.get_ratings_by_recipe_id(db, recipe_id)
    
    if not ratings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No ratings found for the specified recipe")
    
    return ratings