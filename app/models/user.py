from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str | None] = mapped_column(String(200), nullable=True)
    #phone_number: Mapped[str | None] = mapped_column(String(50), nullable=True)
    registration_date: Mapped[str | None] = mapped_column(String(50), nullable=True)
    last_login_date: Mapped[str | None] = mapped_column(String(50), nullable=True)
    email_address: Mapped[str] = mapped_column(String(200), unique=True)
    username: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(200))
    device_list: Mapped[str | None] = mapped_column(Text, nullable=True)
    farm_list: Mapped[str | None] = mapped_column(Text, nullable=True)
    shared_devices: Mapped[str | None] = mapped_column(Text, nullable=True)
    shared_farms: Mapped[str | None] = mapped_column(Text, nullable=True)

