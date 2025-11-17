from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(200))
    phone_number: Mapped[str] = mapped_column(String(50))
    registration_date: Mapped[str] = mapped_column(String(50))
    last_login_date: Mapped[str] = mapped_column(String(50))
    email_address: Mapped[str] = mapped_column(String(200), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(200))
    device_list: Mapped[str] = mapped_column(Text)
    farm_list: Mapped[str] = mapped_column(Text)
    shared_devices: Mapped[str] = mapped_column(Text)
    shared_farms: Mapped[str] = mapped_column(Text)
