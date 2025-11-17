from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    sensor_category = Column(String, nullable=False)
    sensor_product_name = Column(String, nullable=False)
    sensor_serial_number = Column(String, nullable=False)
    name = Column(String, nullable=True)
