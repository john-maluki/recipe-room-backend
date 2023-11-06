from sqlalchemy.orm import Session
from fastapi import  status, HTTPException
from ..models import Favourite, User
from ..schemas import FavouriteRecipe
from typing import List


class FavouriteRecipeRepository:
    def get_favourite_recipe_by_user_and_recipe(user_id: int, recipe_id: int, db: Session):
        return db.query(Favourite).filter_by(user_id=user_id, recipe_id=recipe_id).first()
    
    def create_favourite_recipe(db: Session, user_id: int, recipe_id: int):
        new_favourite_recipe = Favourite(
            user_id=user_id,
            recipe_id=recipe_id,
        )

        db.add(new_favourite_recipe)
        db.commit()

        db.refresh(new_favourite_recipe)

        return new_favourite_recipe
    def get_all_favourite_recipes(db: Session) -> List[FavouriteRecipe]:
        return db.query(Favourite).all()
    
    def get_favourite_recipes_by_user(db: Session, user_id: int) -> List[FavouriteRecipe]:
        return db.query(User).filter_by(id=user_id).first().favourite_recepes
    
    def get_favourite_recipe_by_id(db: Session, favourite_id: int):
        return db.query(Favourite).filter_by(id=favourite_id).first()
    
    def delete_favourite_recipe(db: Session, favourite_id: int):
        favourite_recipe = db.query(Favourite).filter(Favourite.id == favourite_id).first()
        if favourite_recipe:
            db.delete(favourite_recipe)
            db.commit()