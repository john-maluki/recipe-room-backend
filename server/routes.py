from sqlalchemy.orm import Session
from typing import List
from fastapi import Depends, status, HTTPException

from . import app
from .schemas import RecipeSchema, CreateUserSchema, ShowUserSchema
from .database import SessionLocal
from .models import Recipe, User
from .hashing import Hash


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home():
    return {"message": "it is working"}


@app.post("/register", status_code=status.HTTP_201_CREATED, tags=["auths"])
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


@app.get("/users", response_model=List[ShowUserSchema], tags=["users"])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.get(
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


@app.get("/recipes", response_model=List[RecipeSchema], tags=["recipes"])
async def get_recipes(db: Session = Depends(get_db)):
    recipes = db.query(Recipe).all()
    return recipes


@app.get(
    "/recipes/{id}",
    status_code=status.HTTP_200_OK,
    response_model=RecipeSchema,
    tags=["recipes"],
)
async def get_recipe_by_id(id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter_by(id=id).first()
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!"
        )
    return recipe
