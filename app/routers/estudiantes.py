from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import requests

from app.schemas.estudiantes import EstudianteCreate, EstudianteResponse
from app.services.estudiantes import (
    create_estudiante,
    get_estudiante,
    list_estudiantes,
    list_estudiantes_by_acudiente,
)
from app.db import SessionLocal

router = APIRouter()

# URLs de las APIs externas
API_AUTH_URL = "http://127.0.0.1:8009/acudiente"
API_CURSOS_URL = "http://127.0.0.1:8004/cursos"
API_SEDES_URL = "http://127.0.0.1:8000/sedes"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EstudianteResponse)
def create(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    # Validar acudiente
    if estudiante.id_acudiente is not None:
        response = requests.get(f"{API_AUTH_URL}/{estudiante.id_acudiente}")
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Acudiente no válido")

    # Validar curso
    if estudiante.id_curso is not None:
        response = requests.get(f"{API_CURSOS_URL}/{estudiante.id_curso}")
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Curso no válido")

    # Validar sede
    response = requests.get(f"{API_SEDES_URL}/{estudiante.id_sede}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Sede no válida")

    return create_estudiante(db, estudiante)

@router.get("/{id_estudiante}", response_model=EstudianteResponse)
def get(id_estudiante: int, db: Session = Depends(get_db)):
    estudiante = get_estudiante(db, id_estudiante)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

@router.get("/", response_model=list[EstudianteResponse])
def list_all(db: Session = Depends(get_db)):
    return list_estudiantes(db)

@router.get("/por_acudiente/{id_acudiente}", response_model=list[EstudianteResponse])
def list_by_acudiente(id_acudiente: int, db: Session = Depends(get_db)):
    return list_estudiantes_by_acudiente(db, id_acudiente)
