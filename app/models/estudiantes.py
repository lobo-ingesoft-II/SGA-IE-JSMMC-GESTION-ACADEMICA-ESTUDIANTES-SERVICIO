from sqlalchemy import Column, Integer, String, Date, Enum, DateTime
from sqlalchemy.sql import func
from app.db import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id_estudiante = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    tipo_documento = Column(String(20), nullable=False)
    documento_identidad = Column(String(20), nullable=False, unique=True)
    telefono = Column(String(20))
    email = Column(String(100), nullable=False, unique=True)
    fecha_nacimiento = Column(Date)
    id_acudiente = Column(Integer)
    id_curso = Column(Integer)
    id_sede = Column(Integer, nullable=False)
    estado_matricula = Column(
        Enum('pre-matriculado', 'matriculado', 'retirado', name="estado_matricula_enum"),
        default='pre-matriculado',
        nullable=False
    )
    fecha_creacion = Column(DateTime, nullable=False, server_default=func.now())
    fecha_modificacion = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )