from validaciones import validar_menu
from gestionar_prestamo import *

def menu_prestamo():
    while True:
        op_herramienta=validar_menu('''
                        1. Registrar prestamo
                        2. Gestionar prestamo
                        3. Consultar tus prestamos
                        4. Buscar una solicitud de prestamo
                        5. Ver solicitudes prestamo
                        6. Eliminar solicitudes
                        7. Salir
                        ''',1,7)
        match op_herramienta:
            case 1:
                guardar_prestamo()
            case 2:
                gestionar_prestamo()
            case 3:
                consultar_prestamo()
            case 4:
                buscar_prestamo()
            case 5:
                listar_prestamo()
            case 6:
                eliminar_prestamo()
            case 7:
                break
