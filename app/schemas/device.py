from pydantic import BaseModel
from typing import Optional, List, Dict

class DeviceCreate(BaseModel):
    scene: str
    name: str
    icon_path: str
    sensors: List[Dict]
    is_control_type: bool
    product_id: Optional[str]
    serial_number: Optional[str]
    sensor_list: Optional[List[Dict]]
    farm_number: Optional[str]
    shared_devices_with: Optional[List[Dict]]
    automation_setting: Optional[Dict]
    device_password: Optional[str]
    factory_reset_status: Optional[str]
