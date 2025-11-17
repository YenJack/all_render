from pydantic import BaseModel
from typing import Optional

# -------------------------
# Create schema
# -------------------------
class DeviceCreate(BaseModel):
    scene: str
    name: str
    icon_path: str
    sensors: str  # JSON 字串或列表轉字串
    is_control_type: int
    product_id: Optional[str] = None
    serial_number: Optional[str] = None
    sensor_list: Optional[str] = None
    farm_number: Optional[str] = None
    shared_devices_with: Optional[str] = None
    automation_setting: Optional[str] = None
    device_password: Optional[str] = None
    factory_reset_status: Optional[str] = None

# -------------------------
# Read schema
# -------------------------
class DeviceRead(DeviceCreate):
    id: int

    class Config:
        orm_mode = True

# -------------------------
# Update schema
# -------------------------
class DeviceUpdate(BaseModel):
    scene: Optional[str] = None
    name: Optional[str] = None
    icon_path: Optional[str] = None
    sensors: Optional[str] = None
    is_control_type: Optional[int] = None
    product_id: Optional[str] = None
    serial_number: Optional[str] = None
    sensor_list: Optional[str] = None
    farm_number: Optional[str] = None
    shared_devices_with: Optional[str] = None
    automation_setting: Optional[str] = None
    device_password: Optional[str] = None
    factory_reset_status: Optional[str] = None
