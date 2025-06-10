# Servicio de Estudiantes

## Descripción
Este servicio permite gestionar los datos de los estudiantes en el sistema académico. Proporciona funcionalidades para crear, obtener y listar estudiantes, facilitando su integración con otros módulos.

## Endpoints

### Registrar un estudiante
**POST** `/estudiantes/`

#### Request Body
```json
{
  "nombres": "Juan",
  "apellidos": "Pérez",
  "fecha_nacimiento": "2010-05-15",
  "grado": "Primero"
}
```

#### Response

**Status:** 200 OK

```json
{
  "id_estudiante": 1,
  "nombres": "Juan",
  "apellidos": "Pérez",
  "fecha_nacimiento": "2010-05-15",
  "grado": "Primero"
}
```

### Obtener un estudiante por ID

**GET** `/estudiantes/{id_estudiante}`

#### Response

**Status:** 200 OK

```json
{
  "id_estudiante": 1,
  "nombres": "Juan",
  "apellidos": "Pérez",
  "fecha_nacimiento": "2010-05-15",
  "grado": "Primero"
}
```

**Status:** 404 Not Found

```json
{
  "detail": "Estudiante not found"
}
```

### Listar todos los estudiantes

**GET** `/estudiantes/`

#### Response

**Status:** 200 OK

```json
[
  {
    "id_estudiante": 1,
    "nombres": "Juan",
    "apellidos": "Pérez",
    "fecha_nacimiento": "2010-05-15",
    "grado": "Primero"
  },
  {
    "id_estudiante": 2,
    "nombres": "María",
    "apellidos": "Gómez",
    "fecha_nacimiento": "2009-08-20",
    "grado": "Segundo"
  }
]
```

## Instalación

1. Asegúrate de tener el entorno configurado:

   ```bash
   pip install -r requirements.txt
   ```
2. Configura la base de datos en el archivo `.env`:

   ```env
   DATABASE_URL="mysql+pymysql://user:password@host:port/database"
   ```
3. Ejecuta el servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest app/tests/test_estudiantes.py
```

## Dependencias

* **FastAPI**: Framework principal.
* **SQLAlchemy**: ORM para manejar la base de datos.
* **Pytest**: Framework para pruebas unitarias.

## Contacto

Para más información, contactar con el equipo de desarrollo.
