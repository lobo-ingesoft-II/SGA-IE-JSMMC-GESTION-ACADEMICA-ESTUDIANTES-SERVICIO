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
    DATABASE_URL: str = "mysql+pymysql://root:@localhost:3306/estudiantes_db"
    
    # URL del servicio de autenticación
    servidor_api_autenticacion_url: str = Field(default="http://localhost:8009", alias="SERVIDOR_API_AUTENTICACION_URL")
    
    # Configuración general
    SECRET_KEY: str = "prueba123"
    DEBUG: bool = True

    model_config = {"env_file": ".env", "extra": "allow"}

settings = Settings()