from gestionar_json import cargar, guardar, generar_id
from gestionar_usuario import listar_usuario, validar_usuario
from validaciones import validar_entero, validar_menu
from gestionar_herramienta import listar_herramienta, validar_herramienta
from transformaciones import solicitar_fecha_inicio, gestionar, rechazar
from datetime import timedelta

NOMBRE_ARCHIVO = 'prestamos.json'

# --- FUNCIONES HELPER (Privadas del módulo) ---

def _imprimir_prestamo(p):
    """Aplica DRY: Centraliza la visualización de un préstamo."""
    usuario = p.get('usuario', {})
    herramienta = p.get('herramienta', {})
    print(f'''
    ************************************************************
    ID PRESTAMO:    {p.get('id', 'N/A')}
    Usuario:        {usuario.get('nombre', 'Sin nombre')} (ID: {usuario.get('id', 'N/A')})
    Herramienta:    {herramienta.get('nombre', 'Sin nombre')} (ID: {herramienta.get('id', 'N/A')})
    Fecha Inicio:   {p.get('fecha_inicio', 'N/A')}
    Fecha Entrega:  {p.get('fecha_final', 'N/A')}
    Cantidad:       {p.get('cantidad', '0')}
    Estado:         [{p.get('estado', 'En proceso')}]
    Observaciones:  {p.get('observaciones', 'Ninguna')}
    ''')

# --- FUNCIONES PRINCIPALES ---

def guardar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    
    # Datos de Usuario
    listar_usuario()
    id_u = validar_entero('Ingrese el id del usuario: ')
    while not (user_data := validar_usuario(id_u)):
        id_u = validar_entero('Error, usuario no encontrado. Intente nuevamente: ')
    
    # Datos de Herramienta
    listar_herramienta()
    id_h = validar_entero('Ingrese el id de la herramienta: ')
    while not (tool_data := validar_herramienta(id_h)):
        id_h = validar_entero('Error, herramienta no encontrada. Intente nuevamente: ')
    
    # Lógica de Fechas y Cantidad
    cantidad = validar_entero('Ingrese la cantidad de herramientas a solicitar: ')
    fecha_in = solicitar_fecha_inicio()
    dias = validar_entero('Ingrese la cantidad de días a usar la herramienta: ')
    fecha_fin = fecha_in + timedelta(days=dias)
    
    nuevo_prestamo = {
        'id': generar_id(registros),
        'usuario': user_data,
        'herramienta': tool_data,
        'cantidad': cantidad,
        'fecha_inicio': str(fecha_in),
        'fecha_final': str(fecha_fin),
        'estado': 'En proceso',
        'observaciones': 'Pendiente'
    }
    
    registros.append(nuevo_prestamo)
    guardar(NOMBRE_ARCHIVO, registros)
    print(f'\nDATOS GUARDADOS! SU ID DE SEGUIMIENTO ES: {nuevo_prestamo["id"]}')

def listar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print("No hay préstamos registrados.")
    for p in registros:
        _imprimir_prestamo(p)

def consultar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print('No hay registros en este momento.')
        
    id_u = validar_entero('Ingrese el id de Usuario para ver su historial: ')
    encontrado = False
    for p in registros:
        if p.get('usuario', {}).get('id') == id_u:
            _imprimir_prestamo(p)
            encontrado = True
            
    if not encontrado:
        print(f'No se encontraron préstamos para el usuario {id_u}')

def buscar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print('No hay registros para buscar.')
        
    id_buscado = validar_entero("Ingrese el ID del préstamo: ")
    for p in registros:
        if p.get('id') == id_buscado:
            return _imprimir_prestamo(p)
    
    print(f'NO SE ENCONTRÓ EL PRÉSTAMO CON ID: {id_buscado}')

def gestionar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print('No hay registros para gestionar.')
    
    listar_prestamo()
    id_p = validar_entero('Ingrese el id del préstamo a gestionar: ')
    
    for p in registros:
        if p.get('id') == id_p:
            op = validar_menu('\n1. Aprobar/Gestionar\n2. Rechazar\n', 1, 2)
            
            if op == 1:
                gestionar(p.get('herramienta', {}).get('id'), p)
            else:
                rechazar(p)
                
            guardar(NOMBRE_ARCHIVO, registros)
            return print('PRÉSTAMO ACTUALIZADO EXITOSAMENTE.')
            
    print(f'No se encontró el préstamo {id_p}')

def eliminar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print('No hay registros para eliminar.')
    
    listar_prestamo()
    id_e = validar_entero("Ingrese el id a eliminar: ")
    
    for p in registros:
        if p.get('id') == id_e:
            registros.remove(p)
            guardar(NOMBRE_ARCHIVO, registros)
            return print(f'Préstamo {id_e} eliminado del sistema.')
            
    print(f'NO SE ENCONTRÓ EL ID: {id_e}')