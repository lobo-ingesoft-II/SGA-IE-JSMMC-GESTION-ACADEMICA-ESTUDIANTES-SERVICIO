from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.estudiantes import EstudianteCreate, EstudianteResponse
from app.services.estudiantes import create_estudiante, get_estudiante, list_estudiantes
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EstudianteResponse)
def create(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    return create_estudiante(db, estudiante)

@router.get("/{id_estudiante}", response_model=EstudianteResponse)
def get(id_estudiante: int, db: Session = Depends(get_db)):
    db_estudiante = get_estudiante(db, id_estudiante)
    if not db_estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return db_estudiante

@router.get("/", response_model=list[EstudianteResponse])
def list_all(db: Session = Depends(get_db)):
    return list_estudiantes(db)