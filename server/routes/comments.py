from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..repository.comment import CommentRepository
from ..repository.recipe import RecipeRepository
from ..schemas import ShowCommentSchema, CreateCommentSchema
from ..auth.auth_bearer import JWTBearer
from .favourite_recipes import get_user_id


router = APIRouter(prefix="/comments", tags=["comments"])


def recipe_exists(recipe_id: int, db: Session):
    recipe = RecipeRepository.get_recipe_by_id(recipe_id, db)
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!"
        )
    return recipe


@router.post(
    "/",
    response_model=ShowCommentSchema,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
)
async def create_comment(data: CreateCommentSchema, db: Session = Depends(get_db)):
    if not recipe_exists(data.recipe_id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    new_comment = CommentRepository.create_comment(
        db, recipe_id=data.recipe_id, comment=data.comment, user_id=data.user_id
    )
    return new_comment


@router.delete(
    "/{comment_id}",
    response_model=dict,
    dependencies=[Depends(JWTBearer()), Depends(get_user_id)],
)
async def delete_comment(
    comment_id: int, user_id: int = Depends(get_user_id), db: Session = Depends(get_db)
):
    comment = CommentRepository.get_comment_by_id(comment_id, db)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found!"
        )

    if comment.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own comment.",
        )

    CommentRepository.delete_comment(comment_id, db)

    return {"message": "Comment deleted successfully"}


@router.get(
    "/by_recipe/{recipe_id}",
    response_model=List[ShowCommentSchema],
    dependencies=[Depends(JWTBearer())],
)
async def get_comments_by_recipe_id(recipe_id: int, db: Session = Depends(get_db)):
    if not recipe_exists(recipe_id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    comments = CommentRepository.get_comments_by_recipe_id(recipe_id, db)
    return comments


@router.get(
    "/by_user/{user_id}",
    response_model=List[ShowCommentSchema],
    dependencies=[Depends(JWTBearer())],
)
async def get_comments_by_user_id(user_id: int, db: Session = Depends(get_db)):
    comments = CommentRepository.get_comments_by_user_id(user_id, db)
    return comments


@router.get(
    "/{comment_id}",
    response_model=ShowCommentSchema,
    dependencies=[Depends(JWTBearer())],
)
async def get_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    comment = CommentRepository.get_comment_by_id(comment_id, db)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found!"
        )
    return comment
