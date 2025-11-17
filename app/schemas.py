from pydantic import BaseModel
photoDirName: Optional[str]
farmerName: Optional[str]
farmType: Optional[str]
cropName: Optional[str]
farmAddress: Optional[str]
isDeleted: Optional[str]
coordinates: Optional[str]
boundary: Optional[str]
cultivationStatus: Optional[str]
lastModifiedDate: Optional[str]
landArea: Optional[str]
userId: Optional[str]
sharedFarmsWith: Optional[str]


class FarmCreate(FarmBase):
pass


class Farm(FarmBase):
id: int
class Config:
orm_mode = True


# --- devices ---
class DeviceBase(BaseModel):
scene: str
name: str
iconPath: str
sensors: str
isControlType: int
productId: Optional[str]
serialNumber: Optional[str]
sensorList: Optional[str]
farmNumber: Optional[str]
sharedDevicesWith: Optional[str]
automationSetting: Optional[str]
devicePassword: Optional[str]
factoryResetStatus: Optional[str]


class DeviceCreate(DeviceBase):
pass


class Device(DeviceBase):
id: int
class Config:
orm_mode = True


# --- sensors ---
class SensorBase(BaseModel):
sensorCategory: str
sensorProductName: str
sensorSerialNumber: str
name: Optional[str]


class SensorCreate(SensorBase):
pass


class Sensor(SensorBase):
id: int
class Config:
orm_mode = True
