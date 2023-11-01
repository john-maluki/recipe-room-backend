from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository.comment import CommentRepository
from ..repository.recipe import RecipeRepository 
from ..schemas import ShowCommentSchema
from ..auth.auth_bearer import JWTBearer


router = APIRouter(prefix="/comments", tags=["comments"])


def recipe_exists(recipe_id: int, db: Session):
    recipe = RecipeRepository.get_recipe_by_id(recipe_id, db)
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!"
        )
    return recipe

@router.post("/", response_model=ShowCommentSchema, 
             status_code=status.HTTP_201_CREATED, 
             dependencies=[Depends(JWTBearer())])
async def create_comment(
    recipe_id: int,
    comment: str,
    user_id: int,
    db: Session = Depends(get_db)
):

    if not recipe_exists(recipe_id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    new_comment = CommentRepository.create_comment(db, recipe_id=recipe_id, comment=comment, user_id= user_id)
    return new_comment

@router.delete("/{comment_id}", response_model=dict, dependencies=[Depends(JWTBearer())])
async def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = CommentRepository.get_comment_by_id(comment_id, db)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found!"
        )
    
    CommentRepository.delete_comment(comment_id, db)
    
    return {"message": "Comment deleted successfully"}
