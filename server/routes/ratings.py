from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from ..schemas import CreateRatingSchema, ShowRatingSchema, UpdateRatingSchema, ShowUpdatedRatingSchema
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

@router.get("/user/{user_id}", response_model=List[ShowRatingSchema], dependencies=[Depends(JWTBearer())])
async def get_ratings_by_user_id(user_id: int, db: Session = Depends(get_db)):
    ratings = RatingRepository.get_ratings_by_user_id(db, user_id)
    
    if not ratings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No ratings found for the specified user")
    
    return ratings

@router.put("/{rating_id}", response_model=ShowUpdatedRatingSchema, dependencies=[Depends(JWTBearer())])
async def update_rating(rating_id: int, rating_data: UpdateRatingSchema, db: Session = Depends(get_db)):
    existing_rating = RatingRepository.get_rating_by_id(db, rating_id)
    if not existing_rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")

    if existing_rating.user_id != rating_data.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not allowed to update this rating")

    updated_rating = RatingRepository.update_rating(db, rating_id, rating_data)
    return updated_rating