from pydantic import BaseModel
from typing import Optional, List, Dict

class SensorCreate(BaseModel):
    sensor_category: str
    sensor_product_name: str
    sensor_serial_number: str
    name: Optional[str] = None
