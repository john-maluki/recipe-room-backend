from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from ..schemas import ShowUserSchema, UpdateUserSchema
from ..repository.user import UserRepository
from ..database import get_db
from ..auth.auth_bearer import JWTBearer

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/", response_model=List[ShowUserSchema], dependencies=[Depends(JWTBearer())]
)
async def get_users(db: Session = Depends(get_db)):
    users = UserRepository.get_all(db)
    return users


@router.get(
    "/{id}",
    response_model=ShowUserSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = UserRepository.get_user_by_id(id, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
        )
    return user

@router.put(
    "/{id}",
    response_model=ShowUserSchema,
    dependencies=[Depends(JWTBearer())],
)
async def update_user(id: int, user_data: UpdateUserSchema, db: Session = Depends(get_db)):
    existing_user = UserRepository.get_user_by_id(id, db)

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
        )

    updated_user = UserRepository.update_user(existing_user, user_data, db)
    return updated_user
