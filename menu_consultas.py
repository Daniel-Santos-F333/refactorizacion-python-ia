from validaciones import validar_menu
from gestionar_consultas import *

def menu_reportes():
    while True:
        op_herramienta=validar_menu('''
                        __________________________________________
                        /                                          \\
                        |       REPORTE Y CONSULTAS GENERALES      |
                        |__________________________________________/
                        
                        Filtros de información disponibles:
                        
                            [1]  Stock mínimo (Baja disponibilidad)
                            [2]  Solicitudes en proceso / completadas
                            [3]  Buscar solicitudes por usuario
                            [4]  Herramientas más usadas
                            [5]  Usuarios con más prestamos
                            [6]  Volver al menú anterior
                            
                        __________________________________________
                        >>> Selecciona el reporte a generar (1-4):''',1,6)
        match op_herramienta:
            case 1:
                stock_minimo()
            case 2:
                activos_completados()
            case 3:
                historial_usuarios()
            case 4:
                herramienta_mas_usada()
            case 5:
                usuario_mas_usado()
            case 6:
                break