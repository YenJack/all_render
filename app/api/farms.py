# app/api/farms.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.farm import Farm
from app.schemas.farm import FarmCreate, FarmRead, FarmUpdate

router = APIRouter(prefix="/farms", tags=["farms"])

@router.post("/", response_model=FarmRead, status_code=status.HTTP_201_CREATED)
async def create_farm(farm: FarmCreate, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    # 範例：把 current_user.id 存到 farm.user_id
    data = farm.dict()
    data["user_id"] = current_user.id
    new_farm = Farm(**data)
    db.add(new_farm)
    await db.commit()
    await db.refresh(new_farm)
    return new_farm

@router.get("/", response_model=List[FarmRead])
async def get_all_farms(db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    # 只回傳該 user 的 farms（示範）
    result = await db.execute(select(Farm).where(Farm.user_id == str(current_user.id)).order_by(Farm.id.desc()))
    return result.scalars().all()

# 其餘路由同樣加入 current_user: Depends(get_current_user) 並做 owner 驗證（如需要）
