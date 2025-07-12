from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import requests

from app.schemas.estudiantes import EstudianteCreate, EstudianteResponse
from app.services.estudiantes import (
    create_estudiante,
    get_estudiante,
    list_estudiantes,
    list_estudiantes_by_acudiente,
    list_estudiantes_by_curso,
    list_estudiantes_by_asignatura,
)
from app.db import SessionLocal
from app.config import settings

router = APIRouter()

# URLs de las APIs externas (desde configuración)
API_AUTH_URL = f"{settings.servidor_api_autenticacion_url}/acudiente"
API_CURSOS_URL = f"{settings.api_cursos_url}/cursos"
API_SEDES_URL = f"{settings.api_sedes_url}/sedes"

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

@router.get("/por_curso/{id_curso}", response_model=list[EstudianteResponse])
def list_by_curso(id_curso: int, db: Session = Depends(get_db)):
    """
    Obtiene todos los estudiantes asociados a un curso específico.
    
    Args:
        id_curso: ID del curso
    
    Returns:
        Lista de estudiantes matriculados en ese curso
    """
    # Validar que el curso existe
    response = requests.get(f"{API_CURSOS_URL}/{id_curso}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    estudiantes = list_estudiantes_by_curso(db, id_curso)
    if not estudiantes:
        raise HTTPException(status_code=404, detail="No se encontraron estudiantes para este curso")
    return estudiantes

@router.get("/por_asignatura/{id_asignatura}", response_model=list[EstudianteResponse])
def list_by_asignatura(id_asignatura: int, db: Session = Depends(get_db)):
    """
    Obtiene todos los estudiantes asociados a una asignatura específica.
    
    Args:
        id_asignatura: ID de la asignatura
    
    Returns:
        Lista de estudiantes matriculados en cursos que tienen asignada esa asignatura
    """
    estudiantes = list_estudiantes_by_asignatura(db, id_asignatura)
    if not estudiantes:
        raise HTTPException(status_code=404, detail="No se encontraron estudiantes para esta asignatura")
    return estudiantes
