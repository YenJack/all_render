# main.py
import os
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, select

# ---------- DB URL handling (Render may provide "postgres://...") ----------
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    # local fallback for development
    DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/mydb"

# SQLAlchemy async requires scheme "postgresql+asyncpg://"
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)

# ---------- SQLAlchemy async engine & session ----------
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    pool_pre_ping=True,
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

# ---------- Models ----------
class ItemModel(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=True)

# ---------- Pydantic schemas ----------
class ItemCreate(BaseModel):
    name: str
    description: str | None = None

class ItemRead(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        orm_mode = True

# ---------- FastAPI app ----------
app = FastAPI(title="FastAPI + Render Postgres Example")

# Dependency to get async session
async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# Health check
@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/test-db")
async def test_db():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}


# Create item
@app.post("/items", response_model=ItemRead, status_code=201)
async def create_item(payload: ItemCreate, session: AsyncSession = Depends(get_session)):
    item = ItemModel(name=payload.name, description=payload.description)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item

# List items
@app.get("/items", response_model=List[ItemRead])
async def list_items(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(ItemModel).order_by(ItemModel.id))
    items = result.scalars().all()
    return items

# Get specific item
@app.get("/items/{item_id}", response_model=ItemRead)
async def get_item(item_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(ItemModel).where(ItemModel.id == item_id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Optional: create DB tables on startup (only for simple/demo use)
@app.on_event("startup")
async def on_startup():
    # Create tables if not exist — for production use migrations (Alembic)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
