from validaciones import validar_menu
from gestionar_prestamo import *

def menu_prestamo_residente():
    while True:
        op_herramienta=validar_menu('''
                        __________________________________________
                        /                                          \\
                        |       ÁREA RESIDENTE: MIS PRÉSTAMOS      |
                        |__________________________________________/
                        
                        ¿En qué podemos ayudarte hoy?
                        
                            [1]  Solicitar un nuevo préstamo
                            [2]  Consultar el estado de mis préstamos
                            [3]  Volver al menú anterior
                            
                        __________________________________________
                        >>> Selecciona una opción (1-3):''',1,3)
        match op_herramienta:
            case 1:
                guardar_prestamo()
            case 2:
                consultar_prestamo()
            case 3:
                break
