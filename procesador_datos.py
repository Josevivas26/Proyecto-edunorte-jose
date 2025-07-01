# procesador_datos.py
import pandas as pd
from config import Config

class ProcesadorDatos:
    def __init__(self):
        self.config = Config()
    
    def cargar_datos(self):
        """Carga datos desde archivo XLSX"""
        try:
            return pd.read_excel(
                self.config.ARCHIVO_DATOS,
                engine='openpyxl'
            )
        except Exception as e:
            raise Exception(f"Error al cargar {self.config.ARCHIVO_DATOS}: {str(e)}")
    
    def generar_reporte(self, df, limite=None):
        """Genera un reporte básico de los datos"""
        if limite is None:
            limite = self.config.LIMITE_REPORTE
        
        reporte = f"Reporte generado por: {self.config.USUARIO_SISTEMA}\n"
        reporte += f"Total registros: {len(df)}\n"
        reporte += f"Muestra (primeros {limite} registros):\n"
        reporte += str(df.head(limite))
        
        return reporte