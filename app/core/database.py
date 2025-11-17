from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 取得環境變數 DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    # 本地開發用 fallback
    DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/mydb"

# Render 提供的 DATABASE_URL 可能是 postgres://...
# SQLAlchemy async 需要 postgres+asyncpg://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
elif DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

print("Using DATABASE_URL:", DATABASE_URL)

# 建立 async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True
)

# 建立 AsyncSession
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base model
Base = declarative_base()

# Dependency for FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
