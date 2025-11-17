from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.farms import router as farms_router
from app.api.devices import router as devices_router
from app.api.sensors import router as sensors_router

app = FastAPI(title="Farm FastAPI PostgreSQL + JWT")

# 🔥 一定要加 prefix 才會變成 /auth/register
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(farms_router, prefix="/farms", tags=["Farms"])
app.include_router(devices_router, prefix="/devices", tags=["Devices"])
app.include_router(sensors_router, prefix="/sensors", tags=["Sensors"])

@app.get("/")
async def root():
    return {"message": "FastAPI + PostgreSQL + JWT Running 測試"}
