# app/main.py
from fastapi import FastAPI
from app.api.users import router as users_router

app = FastAPI(title="FastAPI + PostgreSQL + Render")

app.include_router(users_router, prefix="/users")

@app.get("/")
def root():
    return {"message": "FastAPI Running"}
