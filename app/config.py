from pydantic import BaseSettings  # Ya incluido en pydantic==1.10.7

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:12345@localhost:3306/estudiantes_db"
    SECRET_KEY: str = "prueba123"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()