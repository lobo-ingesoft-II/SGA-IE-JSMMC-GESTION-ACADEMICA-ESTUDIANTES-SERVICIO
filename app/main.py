from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from app.routers import estudiantes
from app.db import init_db, test_connection
from app.config import settings
from pydantic_settings import BaseSettings
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter, Histogram # type: ignore

app = FastAPI(title="Estudiantes API")

import time
from starlette.requests import Request

# Métricas personalizadas
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total de peticiones HTTP",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Duración de las peticiones HTTP",
    ["method", "endpoint"],
    buckets=[0.1, 0.3, 1.0, 2.5, 5.0, 10.0]
)

ERROR_COUNT = Counter(
    "http_request_errors_total",
    "Total de errores HTTP (status >= 400)",
    ["method", "endpoint", "status_code"]
)

# Middleware para registrar métricas
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
        status_code = response.status_code
    except Exception as e:
        status_code = 500
        raise e
    finally:
        latency = time.time() - start_time
        endpoint = request.url.path
        method = request.method

        REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)
        if status_code >= 400: # type: ignore
            ERROR_COUNT.labels(method=method, endpoint=endpoint, status_code=status_code).inc() # type: ignore

    return response

@app.on_event("startup")
def startup_event():
    init_db()
    test_connection()

#Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_credentials,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
)

#Registrar rutas de estudiantes
app.include_router(estudiantes.router, prefix="/estudiantes", tags=["Estudiantes"])

#Endpoint /metrics para Prometheus
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
