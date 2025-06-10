# Changelog - Servicio de Estudiantes

## [1.0.0] - 2025-06-09
### Agregado
- Creación del servicio de estudiantes.
- Endpoint **POST** `/estudiantes/` para registrar un nuevo estudiante.
- Endpoint **GET** `/estudiantes/{id_estudiante}` para obtener un estudiante por ID.
- Endpoint **GET** `/estudiantes/` para listar todos los estudiantes.
- Integración de modelos, esquemas y servicios con SQLAlchemy y Pydantic.
- Pruebas unitarias básicas para las operaciones CRUD de estudiantes.

## [1.0.1] - 2025-06-09
### Corregido
- Validación de formato de fecha en `fecha_nacimiento`.
- Mejora en los mensajes de error para registros no encontrados.
