from sqlalchemy.orm import Session
from ..models import Recipe


class RecipeRepository:
    def get_all(db: Session):
        recipes = db.query(Recipe).all()
        return recipes

    def get_recipe_by_id(id: int, db: Session):
        recipe = db.query(Recipe).filter_by(id=id).first()
        return recipe
