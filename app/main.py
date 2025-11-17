from fastapi import FastAPI
#from app.api import auth, users, farms, devices, sensors
#from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.farms import router as farms_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(farms_router)


app = FastAPI(title="Farm FastAPI PostgreSQL + JWT")

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(farms.router, prefix="/farms")
app.include_router(devices.router, prefix="/devices")
app.include_router(sensors.router, prefix="/sensors")

@app.get("/")
async def root():
    return {"message": "FastAPI + PostgreSQL + JWT Running 測試"}
