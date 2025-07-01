# main.py
from procesador_datos import ProcesadorDatos
import logging
from config import Config

# Configurar logging
logging.basicConfig(level=Config().LOG_LEVEL)
logger = logging.getLogger(__name__)

def main():
    logger.info("Iniciando procesamiento de datos...")
    
    try:
        procesador = ProcesadorDatos()
        
        # Cargar datos desde XLSX
        datos = procesador.cargar_datos()
        logger.info(f"Datos cargados correctamente. Forma: {datos.shape}")
        
        # Generar reporte
        reporte = procesador.generar_reporte(datos)
        
        # Guardar reporte
        with open('output/reporte_ventas.txt', 'w') as f:
            f.write(reporte)
        
        logger.info("Proceso completado exitosamente")
        
    except Exception as e:
        logger.error(f"Error en el proceso: {str(e)}")
        raise

if __name__ == "__main__":
    main()