from sqlalchemy import Column, Integer, String, Boolean, JSON
from app.core.database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    scene = Column(String, nullable=False)
    name = Column(String, nullable=False)
    icon_path = Column(String, nullable=False)
    sensors = Column(JSON, nullable=False)  # 儲存 sensor id list 或資訊
    is_control_type = Column(Boolean, default=False)
    product_id = Column(String, nullable=True)
    serial_number = Column(String, nullable=True)
    sensor_list = Column(JSON, nullable=True)
    farm_number = Column(String, nullable=True)
    shared_devices_with = Column(JSON, nullable=True)
    automation_setting = Column(JSON, nullable=True)
    device_password = Column(String, nullable=True)
    factory_reset_status = Column(String, nullable=True)
