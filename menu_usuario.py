from validaciones import validar_menu
from gestionar_usuario import *
from logs import historial
def menu_usuario():
    while True:
        op_herramienta=validar_menu('''
                    __________________________________________
                    /                                          \\
                    |       DIRECTORIO: GESTIÓN DE USUARIOS     |
                    |__________________________________________/
                    
                    Administración de Miembros del Vecindario:
                    
                        [1]  Registrar nuevo usuario
                        [2]  Actualizar datos existentes
                        [3]  Listar todos los residentes
                        [4]  Buscar usuario especifíco
                        [5]  Eliminar del sistema
                        [6]  Volver al menú anterior
                        
                    __________________________________________
                    >>> Selecciona una gestión (1-6):''',1,6)
        match op_herramienta:
            case 1:
                guardar_usuario()
                historial('Se ha creado un nuevo usuario ')
            case 2:
                actualizar_usuario()
                historial('Se ha actualizado un usuario ')
            case 3:
                listar_usuario()
            case 4:
                buscar_usuario()
            case 5:
                eliminar_usuario()
                historial('Se ha eliminado un usuario ')
            case 6:
                break