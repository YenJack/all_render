# app/core/config.py
import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    def get_db_url(self) -> str:
        url = self.DATABASE_URL

        if not url:
            # fallback for local dev
            url = "postgresql+asyncpg://postgres:postgres@localhost:5432/mydb"

        # Render 提供的是 postgres:// 需手動換成 sqlalchemy 格式
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+asyncpg://", 1)

        return url

settings = Settings()
