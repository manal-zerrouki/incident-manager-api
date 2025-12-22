from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="Incident Manager API")

# -------------------------
# Page d'accueil (HTML)
# -------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Incident Manager API</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f5f7fa;
                font-family: Arial, Helvetica, sans-serif;
            }
            .container {
                text-align: center;
                background: white;
                padding: 40px 60px;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 2.8rem;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 25px;
                color: #555;
            }
            ul {
                list-style: none;
                padding: 0;
                margin-bottom: 30px;
            }
            li {
                font-size: 1.1rem;
                margin: 10px 0;
            }
            a {
                text-decoration: none;
                color: #2563eb;
                font-weight: bold;
            }
            .footer {
                font-size: 0.95rem;
                color: #777;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚨 Incident Manager API 🚨</h1>
            <p>API backend cloud-native développée avec FastAPI</p>
            <ul>
                <li>🩺 Health check : <a href="/health">/health</a></li>
                <li>📘 Documentation : <a href="/docs">/docs</a></li>
                <li>📂 Incidents (UI) : <a href="/incidents">/incidents</a></li>
                <li>🔌 Incidents (API) : <a href="/api/incidents">/api/incidents</a></li>
            </ul>
            <div class="footer">
                CI/CD · Docker · GitHub Actions · Cloud
            </div>
        </div>
    </body>
    </html>
    """

# -------------------------
# Health check (JSON)
# -------------------------
@app.get("/health", response_class=JSONResponse)
def health():
    return {"status": "ok"}

# -------------------------
# API incidents (JSON)
# -------------------------
incidents = []

@app.get("/api/incidents", response_class=JSONResponse)
def get_incidents():
    return incidents

# -------------------------
# Incidents UI (HTML)
# -------------------------
@app.get("/incidents", response_class=HTMLResponse)
def incidents_page():
    items = "".join(f"<li>{incident}</li>" for incident in incidents)
    content = items if items else "<li>Aucun incident pour le moment</li>"

    return f"""
    <html>
    <head>
        <title>Incidents</title>
        <style>
            body {{
                font-family: Arial;
                background-color: #f5f7fa;
                padding: 40px;
            }}
            h1 {{
                text-align: center;
            }}
            ul {{
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }}
            li {{
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }}
        </style>
    </head>
    <body>
        <h1>📂 Liste des incidents</h1>
        <ul>
            {content}
        </ul>
    </body>
    </html>
    """
