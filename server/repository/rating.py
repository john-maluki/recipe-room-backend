from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from ..models import Rating, User
from ..schemas import CreateRatingSchema, UpdateRatingSchema
from typing import List

class RatingRepository:
    def create_rating(db: Session, rating_data: CreateRatingSchema):
        user_id = rating_data.user_id

        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
            )
        
        new_rating = Rating(
            rating = rating_data.rating,
            user_id=rating_data.user_id,
            recipe_id=rating_data.recipe_id

        )
        db.add(new_rating)
        db.commit()
        db.refresh(new_rating)
        return new_rating
    
    def get_ratings_by_recipe_id(db: Session, recipe_id: int) -> List[Rating]:
        return db.query(Rating).filter(Rating.recipe_id == recipe_id).all()
    
    def get_ratings_by_user_id(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
            )
        return db.query(Rating).filter(Rating.user_id == user_id).all()
    
    def get_rating_by_id(db: Session, rating_id: int):
        return db.query(Rating).filter(Rating.id == rating_id).first()
    
    def update_rating(db: Session, rating_id: int, updated_data: UpdateRatingSchema):
        existing_rating = db.query(Rating).filter(Rating.id == rating_id).first()

        if existing_rating:
            for field, value in updated_data.dict().items():
                setattr(existing_rating, field, value)

            db.commit()
            db.refresh(existing_rating)

        return existing_rating
