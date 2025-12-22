from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers.health import router as health_router
from app.routers.incidents import router as incidents_router

app = FastAPI(
    title="Incident Manager API",
    version="1.0.0",
    description="API backend cloud-native pour la gestion d’incidents (CRUD) avec healthcheck, tests et CI/CD."
)

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Incident Manager API</title>
        <style>
            body { margin:0; height:100vh; display:flex; justify-content:center; align-items:center;
                   background-color:#f5f7fa; font-family:Arial, Helvetica, sans-serif; }
            .container { text-align:center; background:white; padding:40px 60px; border-radius:12px;
                         box-shadow:0 10px 25px rgba(0,0,0,0.1); }
            h1 { font-size:2.8rem; margin-bottom:20px; }
            p { font-size:1.2rem; margin-bottom:25px; color:#555; }
            ul { list-style:none; padding:0; margin-bottom:30px; }
            li { font-size:1.1rem; margin:10px 0; }
            a { text-decoration:none; color:#2563eb; font-weight:bold; }
            .footer { font-size:0.95rem; color:#777; margin-top:20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚨 Incident Manager API 🚨</h1>
            <p>API backend cloud-native développée avec FastAPI</p>
            <ul>
                <li>🩺 Health check : <a href="/health">/health</a></li>
                <li>📘 Documentation : <a href="/docs">/docs</a></li>
                <li>📂 Incidents : <a href="/incidents">/incidents</a></li>
            </ul>
            <div class="footer">CI/CD · Docker · GitHub Actions · Cloud</div>
        </div>
    </body>
    </html>
    """

app.include_router(health_router, tags=["health"])
app.include_router(incidents_router, prefix="/incidents", tags=["incidents"])
