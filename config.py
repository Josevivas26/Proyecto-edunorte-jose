# config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DATABASE_URL = os.getenv('DATABASE_URL')
    ARCHIVO_DATOS = os.getenv('ARCHIVO_DATOS', 'data/datos.xlsx')
    LIMITE_REPORTE = int(os.getenv('LIMITE_REPORTE', 500))
    USUARIO_SISTEMA = os.getenv('USUARIO_SISTEMA')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')