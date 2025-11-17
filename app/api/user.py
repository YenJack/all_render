# app/api/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

@router.post("/", response_model=UserRead)
async def create_user(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    user = User(name=payload.name, email=payload.email)
    db.add(user)

    try:
        await db.commit()
        await db.refresh(user)
    except:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")

    return user

@router.get("/", response_model=list[UserRead])
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()
