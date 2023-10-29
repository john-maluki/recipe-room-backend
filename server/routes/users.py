from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from ..schemas import ShowUserSchema
from ..models import User
from ..database import get_db

router = APIRouter()


@router.get("/users", response_model=List[ShowUserSchema], tags=["users"])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get(
    "/users/{id}",
    response_model=ShowUserSchema,
    status_code=status.HTTP_200_OK,
    tags=["users"],
)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
        )
    return user
