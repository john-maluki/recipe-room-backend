from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from ..models import Rating, User
from ..schemas import CreateRatingSchema
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
    