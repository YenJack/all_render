from pydantic import BaseModel
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    fullName: Optional[str] = None
    phoneNumber: Optional[str] = None
    registrationDate: Optional[str] = None
    lastLoginDate: Optional[str] = None
    emailAddress: Optional[str] = None
    userId: Optional[str] = None
    username: Optional[str] = None
    userPassword: Optional[str] = None
    deviceList: Optional[str] = None
    farmList: Optional[str] = None
    sharedDevices: Optional[str] = None
    sharedFarms: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

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
        from_attributes = True

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
        from_attributes = True

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
        from_attributes = True
