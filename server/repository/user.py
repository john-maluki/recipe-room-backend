from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt

from ..models import User
from ..hashing import Hash


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class UserRepository:
    def get_all(db: Session):
        users = db.query(User).all()
        return users

    def get_user_by_id(id: int, db: Session):
        user = db.query(User).filter_by(id=id).first()
        return user


class AuthRepository:
    def register_user(new_user: User, db: Session):
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def login(username, password, db: Session):
        """
        Fetch user by email and then return it
        """
        user = db.query(User).filter_by(email=username).first()
        if user:
            if not Hash.verify_password(password, user.password):
                return None
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = AuthRepository.create_access_token(
                data={
                    "sub": {
                        "id": user.id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "profile_photo": user.profile_photo,
                        "country": user.country,
                    }
                },
                expires_delta=access_token_expires,
            )
            return {"access_token": access_token}
        return user

    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
