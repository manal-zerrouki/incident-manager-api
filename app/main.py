from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.incidents import router as incidents_router

app = FastAPI(title="Incident Manager API", version="1.0.0")

# endpoint racine 
@app.get("/")
def root():
    return {"message": "Incident Manager API is running"}

app.include_router(health_router, tags=["health"])
app.include_router(incidents_router, prefix="/incidents", tags=["incidents"])
