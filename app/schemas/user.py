# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(..., max_length=50)
    email_address: EmailStr
    password: str = Field(..., max_length=50)  # 字元數限制，不超過 50
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
