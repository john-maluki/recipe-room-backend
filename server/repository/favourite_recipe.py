from sqlalchemy.orm import Session
from ..models import Favourite


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