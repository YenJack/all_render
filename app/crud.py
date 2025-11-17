from sqlalchemy.orm import Session
from app import models, schemas

# User CRUD
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# Farm CRUD
def create_farm(db: Session, farm: schemas.FarmCreate):
    db_farm = models.Farm(**farm.dict())
    db.add(db_farm)
    db.commit()
    db.refresh(db_farm)
    return db_farm

def get_farms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Farm).offset(skip).limit(limit).all()

def get_farm(db: Session, farm_id: int):
    return db.query(models.Farm).filter(models.Farm.id == farm_id).first()

def update_farm(db: Session, farm_id: int, farm: schemas.FarmUpdate):
    db_farm = db.query(models.Farm).filter(models.Farm.id == farm_id).first()
    if db_farm:
        for key, value in farm.dict(exclude_unset=True).items():
            setattr(db_farm, key, value)
        db.commit()
        db.refresh(db_farm)
    return db_farm

def delete_farm(db: Session, farm_id: int):
    db_farm = db.query(models.Farm).filter(models.Farm.id == farm_id).first()
    if db_farm:
        db.delete(db_farm)
        db.commit()
    return db_farm

# Device CRUD
def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_devices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Device).offset(skip).limit(limit).all()

def get_device(db: Session, device_id: int):
    return db.query(models.Device).filter(models.Device.id == device_id).first()

def update_device(db: Session, device_id: int, device: schemas.DeviceUpdate):
    db_device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if db_device:
        for key, value in device.dict(exclude_unset=True).items():
            setattr(db_device, key, value)
        db.commit()
        db.refresh(db_device)
    return db_device

def delete_device(db: Session, device_id: int):
    db_device = db.query(models.Device).filter(models.Device.id == device_id).first()
    if db_device:
        db.delete(db_device)
        db.commit()
    return db_device

# Sensor CRUD
def create_sensor(db: Session, sensor: schemas.SensorCreate):
    db_sensor = models.Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor

def get_sensors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sensor).offset(skip).limit(limit).all()

def get_sensor(db: Session, sensor_id: int):
    return db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()

def update_sensor(db: Session, sensor_id: int, sensor: schemas.SensorUpdate):
    db_sensor = db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()
    if db_sensor:
        for key, value in sensor.dict(exclude_unset=True).items():
            setattr(db_sensor, key, value)
        db.commit()
        db.refresh(db_sensor)
    return db_sensor

def delete_sensor(db: Session, sensor_id: int):
    db_sensor = db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()
    if db_sensor:
        db.delete(db_sensor)
        db.commit()
    return db_sensor
