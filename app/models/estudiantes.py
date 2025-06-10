from sqlalchemy import Column, Integer, String, Date, Enum
from app.db import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id_estudiante = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer)
    id_acudiente = Column(Integer)
    fecha_nacimiento = Column(Date)
    id_curso = Column(Integer)
    estado_matricula = Column(Enum('pre-matriculado', 'matriculado', 'retirado'), default='pre-matriculado')
    sede = Column(String(100))