from pydantic import BaseSettings
import pymysql

class Settings(BaseSettings): # type: ignore
    DATABASE_URL: mysql+pymysql://usuario:contraseña@localhost:3306/estudiantes_db # type: ignore
    SECRET_KEY: prueba123 # type: ignore
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()