from sqlalchemy.orm import Session
from ..models import User


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
