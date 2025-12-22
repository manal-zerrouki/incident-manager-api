from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers.health import router as health_router
from app.routers.incidents import router as incidents_router

app = FastAPI(title="Incident Manager API", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Incident Manager API</title>
        </head>
        <body style="font-family: Arial; background-color: #f4f6f8; padding: 40px;">
            <h1>🚨 Incident Manager API 🚨</h1>
            <p>API backend Cloud-native développée avec FastAPI.</p>

            <ul>
                <li><b>Health check :</b> <a href="/health">/health</a></li>
                <li><b>Documentation :</b> <a href="/docs">/docs</a></li>
                <li><b>Incidents :</b> <code>/incidents</code></li>
            </ul>

            <p style="margin-top:20px; color:gray;">
                CI/CD • Docker • GitHub Actions • Cloud
            </p>
        </body>
    </html>
    """
    
app.include_router(health_router, tags=["health"])
app.include_router(incidents_router, prefix="/incidents", tags=["incidents"])
