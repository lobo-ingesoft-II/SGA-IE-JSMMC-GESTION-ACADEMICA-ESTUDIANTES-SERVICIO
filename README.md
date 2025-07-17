# Servicio de Estudiantes

## Descripción
Este servicio permite gestionar los datos de los estudiantes en el sistema académico. Proporciona funcionalidades para crear, obtener y listar estudiantes, facilitando su integración con otros módulos.

## Endpoints

### Registrar un estudiante
**POST** `/estudiantes/`

#### Request Body
```json
{
  "id_usuario": 1,
  "id_acudiente": 2,
  "fecha_nacimiento": "2010-05-15",
  "id_curso": 3,
  "estado_matricula": "matriculado",
  "sede": "Principal"
}
```

#### Response

**Status:** 200 OK

```json
{
  "id_estudiante": 1,
  "id_usuario": 1,
  "id_acudiente": 2,
  "fecha_nacimiento": "2010-05-15",
  "id_curso": 3,
  "estado_matricula": "matriculado",
  "sede": "Principal"
}
```

### Obtener un estudiante por ID

**GET** `/estudiantes/{id_estudiante}`

#### Response

**Status:** 200 OK

```json
{
  "id_estudiante": 1,
  "id_usuario": 1,
  "id_acudiente": 2,
  "fecha_nacimiento": "2010-05-15",
  "id_curso": 3,
  "estado_matricula": "matriculado",
  "sede": "Principal"
}
```

**Status:** 404 Not Found

```json
{
  "detail": "Estudiante no encontrado"
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
    "id_usuario": 1,
    "id_acudiente": 2,
    "fecha_nacimiento": "2010-05-15",
    "id_curso": 3,
    "estado_matricula": "matriculado",
    "sede": "Principal"
  },
  {
    "id_estudiante": 2,
    "id_usuario": 2,
    "id_acudiente": 3,
    "fecha_nacimiento": "2009-08-20",
    "id_curso": 4,
    "estado_matricula": "pre-matriculado",
    "sede": "Secundaria"
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
   uvicorn app.main:app --reload --port 8005
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

## Documentación interactiva

Accede a la documentación Swagger en [http://localhost:8005/docs](http://localhost:8005/docs) o ReDoc en [http://localhost:8005/redoc](http://localhost:8005/redoc).

## Contacto

Para más información, contactar con el equipo de desarrollo.
