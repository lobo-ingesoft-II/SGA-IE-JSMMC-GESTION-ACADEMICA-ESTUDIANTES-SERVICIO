from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Credenciales MySQL
    host_mysql: str = Field(default="localhost", alias="HOST_MYSQL")
    user_mysql: str = Field(default="root", alias="USER_MYSQL")
    password_mysql: str = Field(default="", alias="PASSWORD_MYSQL")
    database_mysql: str = Field(default="estudiantes_db", alias="DATABASE_MYSQL")
    port_mysql: str = Field(default="3306", alias="PORT_MYSQL")
    
    # URL de la base de datos
    DATABASE_URL: str = "mysql+pymysql://root:1234@localhost:3306/estudiantes_db"

    
    # URL del servicio de autenticación
    servidor_api_autenticacion_url: str = Field(default="http://localhost:8009", alias="SERVIDOR_API_AUTENTICACION_URL")
    
    # URLs de servicios externos
    api_cursos_url: str = Field(default="http://127.0.0.1:8004", alias="API_CURSOS_URL")
    api_sedes_url: str = Field(default="http://127.0.0.1:8007", alias="API_SEDES_URL")
    api_asignaturas_url: str = Field(default="http://127.0.0.1:8001", alias="API_ASIGNATURAS_URL")
    
    # Configuración CORS
    cors_origins: list[str] = Field(default=["*"], alias="CORS_ORIGINS")
    cors_methods: list[str] = Field(default=["*"], alias="CORS_METHODS")
    cors_headers: list[str] = Field(default=["*"], alias="CORS_HEADERS")
    cors_credentials: bool = Field(default=True, alias="CORS_CREDENTIALS")
    
    # Configuración general
    SECRET_KEY: str = "prueba123"
    DEBUG: bool = True

    model_config = {"env_file": ".env", "extra": "allow"} # type: ignore

settings = Settings()