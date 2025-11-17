from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.sensor import Sensor
from app.schemas.sensor import SensorCreate, SensorRead, SensorUpdate

router = APIRouter(prefix="/sensors", tags=["sensors"])

# ---------------------------
# Create Sensor
# ---------------------------
@router.post("/", response_model=SensorRead, status_code=status.HTTP_201_CREATED)
async def create_sensor(sensor: SensorCreate, db: AsyncSession = Depends(get_db)):
    new_sensor = Sensor(**sensor.dict())
    db.add(new_sensor)
    await db.commit()
    await db.refresh(new_sensor)
    return new_sensor

# ---------------------------
# Read all Sensors
# ---------------------------
@router.get("/", response_model=list[SensorRead])
async def get_all_sensors(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Sensor).order_by(Sensor.id.desc()))
    sensors = result.scalars().all()
    return sensors

# ---------------------------
# Read Sensor by ID
# ---------------------------
@router.get("/{sensor_id}", response_model=SensorRead)
async def get_sensor(sensor_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Sensor).where(Sensor.id == sensor_id))
    sensor = result.scalar_one_or_none()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return sensor

# ---------------------------
# Update Sensor
# ---------------------------
@router.put("/{sensor_id}", response_model=SensorRead)
async def update_sensor(sensor_id: int, sensor_update: SensorUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Sensor).where(Sensor.id == sensor_id))
    sensor = result.scalar_one_or_none()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    
    for key, value in sensor_update.dict(exclude_unset=True).items():
        setattr(sensor, key, value)
    
    db.add(sensor)
    await db.commit()
    await db.refresh(sensor)
    return sensor

# ---------------------------
# Delete Sensor
# ---------------------------
@router.delete("/{sensor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sensor(sensor_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Sensor).where(Sensor.id == sensor_id))
    sensor = result.scalar_one_or_none()
    if not sensor:
        raise HTTPException(status_code=404, detail="Sensor not found")
    
    await db.delete(sensor)
    await db.commit()
    return
