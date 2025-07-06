from fastapi import FastAPI
from app.routers import estudiantes
from app.db import init_db, test_connection

app = FastAPI(title="Estudiantes API")

@app.on_event("startup")
def startup_event():
    init_db()
    test_connection()

# Registrar rutas
app.include_router(estudiantes.router, prefix="/estudiantes", tags=["Estudiantes"])