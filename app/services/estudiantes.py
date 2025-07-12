from sqlalchemy.orm import Session
from app.models.estudiantes import Estudiante
from app.schemas.estudiantes import EstudianteCreate
from app.config import settings

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

def list_estudiantes_by_acudiente(db: Session, id_acudiente: int):
    return db.query(Estudiante).filter(Estudiante.id_acudiente == id_acudiente).all()

def list_estudiantes_by_curso(db: Session, id_curso: int):
    """
    Obtiene todos los estudiantes asociados a un curso específico.
    Relación directa: Estudiantes -> Curso (via id_curso)
    """
    return db.query(Estudiante).filter(Estudiante.id_curso == id_curso).all()

def list_estudiantes_by_asignatura(db: Session, id_asignatura: int):
    """
    Obtiene todos los estudiantes asociados a una asignatura específica.
    La relación es: Asignatura -> Curso (via asignacion_asignaturas) -> Estudiantes
    """
    import requests
    
    # Obtener los cursos asociados a la asignatura desde la API de asignaturas
    try:
        # URL del servicio de asignaturas
        API_ASIGNATURAS_URL = f"{settings.api_asignaturas_url}/asignacion_asignaturas"
        response = requests.get(f"{API_ASIGNATURAS_URL}/")
        
        if response.status_code != 200:
            return []
        
        asignaciones = response.json()
        
        # Filtrar las asignaciones que corresponden a la asignatura específica
        cursos_con_asignatura = [
            asignacion["id_curso"] 
            for asignacion in asignaciones 
            if asignacion["id_asignatura"] == id_asignatura
        ]
        
        if not cursos_con_asignatura:
            return []
        
        # Obtener estudiantes que pertenecen a esos cursos
        estudiantes = db.query(Estudiante).filter(
            Estudiante.id_curso.in_(cursos_con_asignatura)
        ).all()
        
        return estudiantes
        
    except Exception as e:
        # En caso de error con la API externa, retornar lista vacía
        return []