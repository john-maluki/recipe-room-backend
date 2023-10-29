from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from ..schemas import CreateUserSchema
from ..models import User
from ..database import get_db
from ..hashing import Hash

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, tags=["auths"])
async def register_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(user.password)
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        email=user.email,
        profile_photo=user.profile_photo,
        country=user.country,
        phone_number=user.phone_number,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
