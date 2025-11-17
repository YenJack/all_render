from fastapi import FastAPI
from app.api import auth, users, farms, devices, sensors

app = FastAPI(title="Farm FastAPI PostgreSQL + JWT")

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(farms.router, prefix="/farms")
app.include_router(devices.router, prefix="/devices")
app.include_router(sensors.router, prefix="/sensors")

@app.get("/")
async def root():
    return {"message": "FastAPI + PostgreSQL + JWT Running 測試"}
