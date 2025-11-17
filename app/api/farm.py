from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.farm import Farm
from app.schemas.farm import FarmCreate, FarmRead, FarmUpdate

router = APIRouter(prefix="/farms", tags=["farms"])

# ---------------------------
# Create Farm
# ---------------------------
@router.post("/", response_model=FarmRead, status_code=status.HTTP_201_CREATED)
async def create_farm(farm: FarmCreate, db: AsyncSession = Depends(get_db)):
    new_farm = Farm(**farm.dict())
    db.add(new_farm)
    await db.commit()
    await db.refresh(new_farm)
    return new_farm

# ---------------------------
# Read all Farms
# ---------------------------
@router.get("/", response_model=list[FarmRead])
async def get_all_farms(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Farm).order_by(Farm.id.desc()))
    farms = result.scalars().all()
    return farms

# ---------------------------
# Read Farm by ID
# ---------------------------
@router.get("/{farm_id}", response_model=FarmRead)
async def get_farm(farm_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Farm).where(Farm.id == farm_id))
    farm = result.scalar_one_or_none()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm

# ---------------------------
# Update Farm
# ---------------------------
@router.put("/{farm_id}", response_model=FarmRead)
async def update_farm(farm_id: int, farm_update: FarmUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Farm).where(Farm.id == farm_id))
    farm = result.scalar_one_or_none()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    
    for key, value in farm_update.dict(exclude_unset=True).items():
        setattr(farm, key, value)
    
    db.add(farm)
    await db.commit()
    await db.refresh(farm)
    return farm

# ---------------------------
# Delete Farm
# ---------------------------
@router.delete("/{farm_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_farm(farm_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Farm).where(Farm.id == farm_id))
    farm = result.scalar_one_or_none()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    
    await db.delete(farm)
    await db.commit()
    return
