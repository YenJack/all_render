from pydantic import BaseModel
from typing import Optional, List, Dict

# ---------------------------
# Base schema
# ---------------------------
class FarmBase(BaseModel):
    lat: float
    lon: float
    farm_name: Optional[str] = None
    farm_number: Optional[str] = None
    device_array: Optional[List[Dict]] = None
    photo_dir_name: Optional[str] = None
    farmer_name: Optional[str] = None
    farm_type: Optional[str] = None
    crop_name: Optional[str] = None
    farm_address: Optional[str] = None
    is_deleted: Optional[bool] = False
    coordinates: Optional[List[List[float]]] = None  # e.g., 边界座標
    boundary: Optional[List[List[float]]] = None
    cultivation_status: Optional[str] = None
    last_modified_date: Optional[str] = None
    land_area: Optional[str] = None
    user_id: Optional[int] = None
    shared_farms_with: Optional[List[int]] = None

# ---------------------------
# Create schema
# ---------------------------
class FarmCreate(FarmBase):
    pass

# ---------------------------
# Update schema
# ---------------------------
class FarmUpdate(FarmBase):
    pass

# ---------------------------
# Read schema
# ---------------------------
class FarmRead(FarmBase):
    id: int

    class Config:
        orm_mode = True
