import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 從環境變數取得資料庫連接字串
DATABASE_URL = os.getenv("DATABASE_URL")

# 如果 DATABASE_URL 以 postgres:// 開頭，需要替換為 postgresql://
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 如果沒有環境變數，使用預設值（用於本地開發）
if not DATABASE_URL:
    DATABASE_URL = "postgresql://username:password@localhost/harvest_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
