from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..database import SessionLocal

from ..models import User
from ..schemas import UpdateUserSchema
from ..hashing import Hash
from ..auth.auth_handler import signJWT


class UserRepository:
    def get_all(db: Session):
        users = db.query(User).all()
        return users

    def get_user_by_id(id: int, db: Session):
        user = db.query(User).filter_by(id=id).first()
        return user
    
    def update_user(existing_user: User, user_data: UpdateUserSchema, db: Session):
        data_dict = user_data.dict()

        for key, value in data_dict.items():
            setattr(existing_user, key, value)

        db.commit()
        db.refresh(existing_user)

        return existing_user
    
    def delete_user(user_id: int, db: Session):
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found!"
            )

        db.delete(user)
        db.commit()

        return {"message": f"User with id {user_id} has been deleted"}


class AuthRepository:
    def get_user(id):
        session = SessionLocal()
        user = session.query(User).filter_by(id=id).first()
        return user

    def register_user(new_user: User, db: Session):
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def login(email, password, db: Session):
        """
        Fetch user by email and then return it
        """
        user = db.query(User).filter_by(email=email).first()
        if user:
            if not Hash.verify_password(password, user.password):
                return None
        return user

    def create_access_token(user):
        return signJWT(user)
