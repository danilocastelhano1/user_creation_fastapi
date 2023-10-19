import models

from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from typing import List

from sqlalchemy.orm import Session

from schemas import UserCreateSchema
from schemas import UserResponseSchema

from repositories.user_repository import UserRepository

from database import get_db
from database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/user", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = UserRepository().get_user_by_email(db, user_email=user.email)
    if db_user:
         raise HTTPException(
                  status_code=status.HTTP_400_BAD_REQUEST,
                  detail="User already registered")
    db_user = UserRepository().create(db=db, user=user)

    return UserResponseSchema.from_orm(db_user)


@app.get("/user", response_model=List[UserResponseSchema], status_code=status.HTTP_200_OK)
def get_all_user(db: Session = Depends(get_db)):
    all_users = UserRepository.get_all(db)
    return [UserResponseSchema.from_orm(user) for user in all_users]
