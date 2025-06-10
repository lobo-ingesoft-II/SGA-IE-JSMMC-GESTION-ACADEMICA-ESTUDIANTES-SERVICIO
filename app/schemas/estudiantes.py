from pydantic import BaseModel
from datetime import date

class EstudianteBase(BaseModel):
    nombres: str
    apellidos: str
    fecha_nacimiento: date
    grado: str

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteResponse(EstudianteBase):
    id_estudiante: int

    class Config:
        orm_mode = True