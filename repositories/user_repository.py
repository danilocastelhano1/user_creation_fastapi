from sqlalchemy.orm import Session

from typing import Dict, List, Type
from typing import List
from typing import Optional

from models import User
from models import Role

from repositories.role_repository import RoleRepository
from schemas import UserCreateSchema
from schemas import CreateRoleSchema

from utils import generate_random_password


class UserRepository:
    @staticmethod
    def create(db: Session, user: UserCreateSchema):
        user_dict: Dict = user.model_dump()
        if not user_dict["password"]:
            user_dict["password"] = generate_random_password()

        role_db: Optional[Role] = RoleRepository().create(
            db=db,
            role=CreateRoleSchema(description=user_dict.pop("role"))
        )

        user_dict["role_id"] = role_db.id

        db_user = User(**user_dict)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_email(db: Session, user_email: str):
        return db.query(User).filter(User.email == user_email).first()

    @staticmethod
    def get_all(db: Session) -> list[Type[User]]:
        return db.query(User).all()
