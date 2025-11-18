# app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User
from app.schemas.user import UserCreate, Token

router = APIRouter(tags=["auth"])


@router.post("/register", response_model=Token)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    # 檢查 username/email 是否存在
    result = await db.execute(select(User).where(User.username == user_in.username))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    u = User(
        username=user_in.username,
        email_address=user_in.email_address,
        full_name=user_in.full_name or "",
        phone_number=user_in.phone_number or "",
        registration_date=datetime.now().isoformat(),
        last_login_date="",
        hashed_password=hash_password(user_in.password),
        device_list="[]",
        farm_list="[]",
        shared_devices="[]",
        shared_farms="[]",
    )
    db.add(u)
    await db.commit()
    await db.refresh(u)

    access_token = create_access_token({"sub": u.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    # OAuth2PasswordRequestForm has .username and .password
    result = await db.execute(select(User).where(User.username == form_data.username))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
