from pydantic import BaseModel
from typing import Optional, Literal
from datetime import date

class EstudianteBase(BaseModel):
    id_usuario: Optional[int] = None
    id_acudiente: Optional[int] = None
    fecha_nacimiento: Optional[date] = None
    id_curso: Optional[int] = None
    estado_matricula: Optional[Literal['pre-matriculado', 'matriculado', 'retirado']] = 'pre-matriculado'
    sede: Optional[str] = None

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteResponse(EstudianteBase):
    id_estudiante: int

    class Config:
        orm_mode = True