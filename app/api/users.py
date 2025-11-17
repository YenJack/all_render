# app/api/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.user import UserRead, UserCreate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserRead])
async def list_users(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    # current_user 可用於權限判斷
    result = await db.execute(select(User))
    return result.scalars().all()


@router.get("/me", response_model=UserRead)
async def read_me(current_user: User = Depends(get_current_user)):
    return current_user

# 其餘 create/update/delete 若要保護也加入 Depends(get_current_user)
