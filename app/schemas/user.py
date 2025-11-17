# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str
    email_address: str
    password: str = Field(..., max_length=72)
    full_name: str | None = None

class UserRead(BaseModel):
    id: int
    username: str
    email_address: str
    full_name: str | None = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
