from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from ..models import Recipe, User
from ..schemas import CreateRecipeSchema, UpdateRecipeSchema
from typing import List


class RecipeRepository:
    def create_recipe(db: Session, recipe_data: CreateRecipeSchema):
        user_id = recipe_data.user_id

        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
            )

        new_recipe = Recipe(
            name=recipe_data.name,
            recipe_image=recipe_data.recipe_image,
            ingredients=recipe_data.ingredients,
            procedure=recipe_data.procedure,
            number_of_people_served=recipe_data.number_of_people_served,
            time_in_minutes=recipe_data.time_in_minutes,
            country=recipe_data.country,
            user=user,  
        )

        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
        return new_recipe
    
    def get_all(db: Session):
        recipes = db.query(Recipe).all()
        return recipes

    def get_recipe_by_id(id: int, db: Session):
        recipe = db.query(Recipe).filter_by(id=id).first()
        return recipe
    
    def get_recipes_by_user(user_id: int, db: Session) -> List[Recipe]:
        recipes = db.query(Recipe).filter(Recipe.user_id == user_id).all()
        return recipes
    
    def update_recipe(db: Session, existing_recipe: Recipe, recipe_data: UpdateRecipeSchema):
        data_dict = recipe_data.dict()

        for key, value in data_dict.items():
            setattr(existing_recipe, key, value)

        db.commit()
        db.refresh(existing_recipe)

        return existing_recipe
    
    def delete_recipe(id: int, db: Session):
        recipe = db.query(Recipe).filter_by(id=id).first()

        if not recipe:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Recipe with id {id} not found!"
            )

        db.delete(recipe)
        db.commit()

        return {"message": f"Recipe with id {id} has been deleted"}
