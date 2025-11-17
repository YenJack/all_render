import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    def get_db_url(self) -> str:
        url = self.DATABASE_URL
        if not url:
            url = "postgresql+asyncpg://postgres:postgres@localhost:5432/mydb"
        # 確保 asyncpg
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+asyncpg://", 1)
        elif url.startswith("postgresql://") and not url.startswith("postgresql+asyncpg://"):
            url = url.replace("postgresql://", "postgresql+asyncpg://", 1)
        return url

settings = Settings()
