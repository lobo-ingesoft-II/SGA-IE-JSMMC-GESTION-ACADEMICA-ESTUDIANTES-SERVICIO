from sqlalchemy.orm import Session
from app.models.estudiantes import Estudiante
from app.schemas.estudiantes import EstudianteCreate

def create_estudiante(db: Session, estudiante: EstudianteCreate):
    db_estudiante = Estudiante(**estudiante.dict())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

def get_estudiante(db: Session, id_estudiante: int):
    return db.query(Estudiante).filter(Estudiante.id_estudiante == id_estudiante).first()

def list_estudiantes(db: Session):
    return db.query(Estudiante).all()