from sqlalchemy.orm import Session
from ..database import SessionLocal

from ..models import User
from ..hashing import Hash
from ..auth.auth_handler import signJWT


class UserRepository:
    def get_all(db: Session):
        users = db.query(User).all()
        return users

    def get_user_by_id(id: int, db: Session):
        user = db.query(User).filter_by(id=id).first()
        return user


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
