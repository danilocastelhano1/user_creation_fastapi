from sqlalchemy.orm import Session

from typing import Optional

from schemas import CreateRoleSchema
from models import Role


class RoleRepository:
    @staticmethod
    def create(db: Session, role: CreateRoleSchema):
        db_role: Optional[Role] = db.query(Role).filter(Role.description == role.description).first()
        if not db_role:
            db_role = Role(**role.model_dump())
            db.add(db_role)
            db.commit()
            db.refresh(db_role)

        return db_role
