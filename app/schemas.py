from pydantic import BaseModel
from typing import Optional, List

# User Schemas
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str | None] = mapped_column(String(200), nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(50), nullable=True)
    registration_date: Mapped[str | None] = mapped_column(String(50), nullable=True)
    last_login_date: Mapped[str | None] = mapped_column(String(50), nullable=True)
    email_address: Mapped[str] = mapped_column(String(200), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(200))
    device_list: Mapped[str | None] = mapped_column(Text, nullable=True)
    farm_list: Mapped[str | None] = mapped_column(Text, nullable=True)
    shared_devices: Mapped[str | None] = mapped_column(Text, nullable=True)
    shared_farms: Mapped[str | None] = mapped_column(Text, nullable=True)

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True  # Pydantic v1 使用 orm_mode

# Farm Schemas
class FarmBase(BaseModel):
    lat: float
    lon: float
    farmName: Optional[str] = None
    farmNumber: Optional[str] = None
    deviceArray: Optional[str] = None
    photoDirName: Optional[str] = None
    farmerName: Optional[str] = None
    farmType: Optional[str] = None
    cropName: Optional[str] = None
    farmAddress: Optional[str] = None
    isDeleted: Optional[str] = None
    coordinates: Optional[str] = None
    boundary: Optional[str] = None
    cultivationStatus: Optional[str] = None
    lastModifiedDate: Optional[str] = None
    landArea: Optional[str] = None
    userId: Optional[str] = None
    sharedFarmsWith: Optional[str] = None

class FarmCreate(FarmBase):
    pass

class FarmUpdate(FarmBase):
    pass

class Farm(FarmBase):
    id: int

    class Config:
        orm_mode = True

# Device Schemas
class DeviceBase(BaseModel):
    scene: str
    name: str
    iconPath: str
    sensors: str
    isControlType: int
    productId: Optional[str] = None
    serialNumber: Optional[str] = None
    sensorList: Optional[str] = None
    farmNumber: Optional[str] = None
    sharedDevicesWith: Optional[str] = None
    automationSetting: Optional[str] = None
    devicePassword: Optional[str] = None
    factoryResetStatus: Optional[str] = None

class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int

    class Config:
        orm_mode = True

# Sensor Schemas
class SensorBase(BaseModel):
    sensorCategory: str
    sensorProductName: str
    sensorSerialNumber: str
    name: Optional[str] = None

class SensorCreate(SensorBase):
    pass

class SensorUpdate(SensorBase):
    pass

class Sensor(SensorBase):
    id: int

    class Config:
        orm_mode = True
