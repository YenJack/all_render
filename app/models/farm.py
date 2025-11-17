from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
from app.core.database import Base

class Farm(Base):
    __tablename__ = "farms"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    lat: Mapped[float] = mapped_column(Float)
    lon: Mapped[float] = mapped_column(Float)
    farm_name: Mapped[str] = mapped_column(String(200))
    farm_number: Mapped[str] = mapped_column(String(100))
    device_array: Mapped[str] = mapped_column(Text)
    photo_dir_name: Mapped[str] = mapped_column(String(200))
    farmer_name: Mapped[str] = mapped_column(String(200))
    farm_type: Mapped[str] = mapped_column(String(100))
    crop_name: Mapped[str] = mapped_column(String(100))
    farm_address: Mapped[str] = mapped_column(String(200))
    is_deleted: Mapped[str] = mapped_column(String(10))
    coordinates: Mapped[str] = mapped_column(Text)
    boundary: Mapped[str] = mapped_column(Text)
    cultivation_status: Mapped[str] = mapped_column(String(100))
    last_modified_date: Mapped[str] = mapped_column(String(50))
    land_area: Mapped[str] = mapped_column(String(50))
    user_id: Mapped[str] = mapped_column(String(100))
    shared_farms_with: Mapped[str] = mapped_column(Text)
