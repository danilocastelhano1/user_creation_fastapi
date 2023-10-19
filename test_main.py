from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from database import get_db

from fastapi import status
from fastapi.testclient import TestClient

from main import app

from typing import Dict

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

default_data: Dict = {
    "name": "João da Silva",
    "email": "joao_silva@outlook.com",
    "role": "gerente"
}


def test_post_without_informing_password():
    response = client.post("/user", json=default_data)
    assert response.status_code == status.HTTP_201_CREATED


def test_post_informing_password():
    password: str = "teste@123"
    default_data["email"] = "joao_silva_2@outlook.com"
    default_data["password"] = password
    response = client.post("/user", json=default_data)
    print("here", response.json())
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["password"] == password
