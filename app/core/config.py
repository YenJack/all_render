import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    def get_db_url(self) -> str:
        url = self.DATABASE_URL
        if not url:
            url = "postgresql+asyncpg://postgres:postgres@localhost:5432/mydb"
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql+asyncpg://", 1)
        return url

settings = Settings()
