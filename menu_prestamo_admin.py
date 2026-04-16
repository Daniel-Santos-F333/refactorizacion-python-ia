from validaciones import validar_menu
from gestionar_prestamo import *
from logs import historial

def menu_prestamo_admin():
    while True:
        op_herramienta=validar_menu('''
                        __________________________________________
                        /                                          \\
                        |       LOGÍSTICA: GESTIÓN DE PRÉSTAMOS     |
                        |__________________________________________/
                        
                        Panel de Control de Préstamos y Devoluciones:
                        
                            [1] Gestionar préstamos
                            [2] Buscar una solicitud específica
                            [3] Ver todas las solicitudes
                            [4] Eliminar registros de solicitudes
                            [5] Volver al menú anterior
                            
                        __________________________________________
                        >>> Selecciona una opción (1-5):''',1,5)
        match op_herramienta:
            case 1:
                gestionar_prestamo()
                historial('Se ha gestionado una solicitud de prestamo ')
            case 2:
                buscar_prestamo()
            case 3:
                listar_prestamo()
            case 4:
                eliminar_prestamo()
                historial('Se ha eliminado una solicitod de prestamo ')
            case 5:
                break
