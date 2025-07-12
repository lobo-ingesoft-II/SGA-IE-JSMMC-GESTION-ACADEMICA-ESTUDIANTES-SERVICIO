from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import estudiantes
from app.db import init_db, test_connection
from app.config import settings

app = FastAPI(title="Estudiantes API")

@app.on_event("startup")
def startup_event():
    init_db()
    test_connection()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,  # Configurable desde .env
    allow_credentials=settings.cors_credentials,
    allow_methods=settings.cors_methods,  # Configurable desde .env
    allow_headers=settings.cors_headers,  # Configurable desde .env
)

# Registrar rutas
app.include_router(estudiantes.router, prefix="/estudiantes", tags=["Estudiantes"])