from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import requests

from app.schemas.estudiantes import EstudianteCreate, EstudianteResponse
from app.services.estudiantes import (
    create_estudiante,
    get_estudiante,
    list_estudiantes,
    list_estudiantes_by_acudiente, # type: ignore
)
from app.db import SessionLocal

router = APIRouter()

# URLs de las APIs externas (ajusta según tu entorno)
API_AUTH_URL = "http://127.0.0.1:8001/usuarios"
API_CURSOS_URL = "http://127.0.0.1:8002/cursos"
API_SEDES_URL = "http://127.0.0.1:8003/sedes"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Crear estudiante con validaciones externas ---
@router.post("/", response_model=EstudianteResponse)
def create(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    # Validar id_acudiente en API de Autenticación (si viene)
    if estudiante.id_acudiente is not None:
        resp = requests.get(f"{API_AUTH_URL}/{estudiante.id_acudiente}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="id_acudiente no existe en autenticación")

    # Validar id_curso en API de Cursos (si viene)
    if estudiante.id_curso is not None:
        resp = requests.get(f"{API_CURSOS_URL}/{estudiante.id_curso}")
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail="id_curso no existe en cursos")

    # Validar id_sede en API de Sedes
    resp = requests.get(f"{API_SEDES_URL}/{estudiante.id_sede}")
    if resp.status_code != 200:
        raise HTTPException(status_code=400, detail="id_sede no existe en sedes")

    return create_estudiante(db, estudiante)

# --- Obtener estudiante por id_estudiante ---
@router.get("/{id_estudiante}", response_model=EstudianteResponse)
def get(id_estudiante: int, db: Session = Depends(get_db)):
    db_estudiante = get_estudiante(db, id_estudiante)
    if not db_estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante

# --- Listar todos los estudiantes ---
@router.get("/", response_model=list[EstudianteResponse])
def list_all(db: Session = Depends(get_db)):
    return list_estudiantes(db)

# --- Listar estudiantes por id_acudiente ---
@router.get("/por_acudiente/{id_acudiente}", response_model=list[EstudianteResponse])
def list_by_acudiente(id_acudiente: int, db: Session = Depends(get_db)):
    estudiantes = list_estudiantes_by_acudiente(db, id_acudiente)
    return estudiantes
