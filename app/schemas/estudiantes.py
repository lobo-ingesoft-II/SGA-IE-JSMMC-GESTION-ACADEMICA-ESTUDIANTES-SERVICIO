from pydantic import BaseModel, EmailStr
from typing import Optional, Literal
from datetime import date, datetime

class EstudianteBase(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: str
    documento_identidad: str
    telefono: Optional[str] = None
    email: EmailStr
    fecha_nacimiento: Optional[date] = None
    id_acudiente: Optional[int] = None
    id_curso: Optional[int] = None
    id_sede: int
    estado_matricula: Optional[Literal['pre-matriculado', 'matriculado', 'retirado']] = 'pre-matriculado'

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteResponse(EstudianteBase):
    id_estudiante: int
    fecha_creacion: datetime
    fecha_modificacion: datetime

    class Config:
        orm_mode = True
