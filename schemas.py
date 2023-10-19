from pydantic import BaseModel
from datetime import datetime


class RoleSchema(BaseModel):
    id: int
    description: str

    class Config:
        from_attributes = True


class CreateRoleSchema(BaseModel):
    description: str


class BaseUserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str
    role: RoleSchema
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    name: str
    email: str
    password: str = ""
    role: str


class UserResponseSchema(BaseUserSchema):
    class Config:
        from_attributes = True
