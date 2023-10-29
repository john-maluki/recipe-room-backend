from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

from ..schemas import CreateUserSchema, LoginSchema
from ..models import User
from ..repository.user import AuthRepository
from ..database import get_db
from ..hashing import Hash

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
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
    return AuthRepository.register_user(new_user, db)


@router.post("/login")
async def login(
    user_credentials: LoginSchema,
    db: Session = Depends(get_db),
):
    user = AuthRepository.login(
        user_credentials.username, user_credentials.password, db
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials!"
        )
    access_token = AuthRepository.create_access_token(user)
    return access_token
