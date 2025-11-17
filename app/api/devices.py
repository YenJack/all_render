from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.device import Device
from app.schemas.device import DeviceCreate, DeviceRead, DeviceUpdate

router = APIRouter(prefix="/devices", tags=["devices"])

# ---------------------------
# Create Device
# ---------------------------
@router.post("/", response_model=DeviceRead, status_code=status.HTTP_201_CREATED)
async def create_device(device: DeviceCreate, db: AsyncSession = Depends(get_db)):
    new_device = Device(**device.dict())
    db.add(new_device)
    await db.commit()
    await db.refresh(new_device)
    return new_device

# ---------------------------
# Read all Devices
# ---------------------------
@router.get("/", response_model=list[DeviceRead])
async def get_all_devices(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Device).order_by(Device.id.desc()))
    devices = result.scalars().all()
    return devices

# ---------------------------
# Read Device by ID
# ---------------------------
@router.get("/{device_id}", response_model=DeviceRead)
async def get_device(device_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Device).where(Device.id == device_id))
    device = result.scalar_one_or_none()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

# ---------------------------
# Update Device
# ---------------------------
@router.put("/{device_id}", response_model=DeviceRead)
async def update_device(device_id: int, device_update: DeviceUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Device).where(Device.id == device_id))
    device = result.scalar_one_or_none()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    
    for key, value in device_update.dict(exclude_unset=True).items():
        setattr(device, key, value)
    
    db.add(device)
    await db.commit()
    await db.refresh(device)
    return device

# ---------------------------
# Delete Device
# ---------------------------
@router.delete("/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_device(device_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Device).where(Device.id == device_id))
    device = result.scalar_one_or_none()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    
    await db.delete(device)
    await db.commit()
    return
