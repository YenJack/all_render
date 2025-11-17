from pydantic import BaseModel
from typing import Optional

# -------------------------
# Create schema
# -------------------------
class SensorCreate(BaseModel):
    sensor_category: str
    sensor_product_name: str
    sensor_serial_number: str
    name: Optional[str] = None

# -------------------------
# Read schema
# -------------------------
class SensorRead(SensorCreate):
    id: int

    class Config:
        orm_mode = True

# -------------------------
# Update schema
# -------------------------
class SensorUpdate(BaseModel):
    sensor_category: Optional[str] = None
    sensor_product_name: Optional[str] = None
    sensor_serial_number: Optional[str] = None
    name: Optional[str] = None
