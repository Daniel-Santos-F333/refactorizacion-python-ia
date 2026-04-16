from validaciones import validar_menu, validar_texto, validar_entero
import gestionar_json as gestor

# Constantes
NOMBRE_ARCHIVO = 'categorias.json'

# --- Funciones de Utilidad (Privadas/Internas) ---

def _obtener_datos():
    """Centraliza la carga de datos."""
    return gestor.cargar(NOMBRE_ARCHIVO)

def _guardar_datos(registros):
    """Centraliza el guardado de datos."""
    gestor.guardar(NOMBRE_ARCHIVO, registros)

def _buscar_por_id(registros, id_buscado):
    """Busca un elemento en la lista por su ID. (Principio DRY)"""
    for elemento in registros:
        if elemento.get('id') == id_buscado:
            return elemento
    return None

def _imprimir_formato(elemento):
    """Estandariza la visualización de la categoría."""
    print(f'''
            *********************************************************
            id:             {elemento.get('id', 'N/A')}
            categoria:      {elemento.get('nombre', 'Sin nombre')}
            ''')

# --- Funciones Principales ---

def guardar_categoria():
    registros = _obtener_datos()
    nueva_categoria = {
        'id': gestor.generar_id(registros),
        'nombre': validar_texto('Ingrese la categoria de la herramienta: ', 1, 30)
    }
    registros.append(nueva_categoria)
    _guardar_datos(registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')

def listar_categoria():
    registros = _obtener_datos()
    if not registros:
        print("No hay registros para mostrar.")
        return
    for elemento in registros:
        _imprimir_formato(elemento)

def buscar_categoria():
    registros = _obtener_datos()
    if not registros:
        print('No se puede buscar porque no hay registros')
        return

    id_buscado = validar_entero("Ingrese el id a buscar: ")
    elemento = _buscar_por_id(registros, id_buscado)
    
    if elemento:
        _imprimir_formato(elemento)
    else:
        print(f'NO SE ENCONTRÓ EL ID: {id_buscado}')

def validar_categoria(id_buscado):
    """Retorna un diccionario compatible con la estructura original."""
    registros = _obtener_datos()
    elemento = _buscar_por_id(registros, id_buscado)
    
    if elemento:
        return {
            'id': elemento.get('id'),
            'categoria': elemento.get('nombre')
        }
    return False

def actualizar_categoria():
    registros = _obtener_datos()
    if not registros:
        print('No se puede actualizar porque no hay registros')
        return

    listar_categoria()
    id_buscado = validar_entero("Ingrese el id a actualizar: ")
    elemento = _buscar_por_id(registros, id_buscado)

    if not elemento:
        print(f'NO SE ENCONTRÓ EL ID: {id_buscado}')
        return

    opcion = validar_menu('''
                            1. Nombre Categoria.
                            2. Cancelar 
                            ''', 1, 2)
    if opcion == 1:
        elemento['nombre'] = validar_texto('Ingrese la nueva categoria: ', 1, 20)
        _guardar_datos(registros)
        print('DATO ACTUALIZADO!')
    else:
        print('Operación cancelada!')

def eliminar_categoria():
    registros = _obtener_datos()
    if not registros:
        print('No se puede eliminar porque no hay registros')
        return

    listar_categoria()
    id_buscado = validar_entero("Ingrese el id a eliminar: ")
    elemento = _buscar_por_id(registros, id_buscado)

    if elemento:
        print(f"{elemento.get('nombre')} ya no está entre nosotros!")
        registros.remove(elemento)
        _guardar_datos(registros)
    else:
        print(f'NO SE ENCONTRÓ EL ID: {id_buscado}')