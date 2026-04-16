from validaciones import validar_menu, validar_texto, validar_entero
from gestionar_json import cargar, guardar, generar_id

NOMBRE_ARCHIVO = 'categorias.json'

def _imprimir_item_categoria(elemento):
    """Función privada para estandarizar la salida."""
    print(f'''
    *********************************************************
    ID:             {elemento.get("id", "N/A")}
    Categoría:      {elemento.get("nombre", "Sin nombre")}
    ''')

def guardar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    nueva_cat = {
        "id": generar_id(registros),
        "nombre": validar_texto('Ingrese la categoria de la herramienta: ', 1, 30)
    }
    registros.append(nueva_cat)
    guardar(NOMBRE_ARCHIVO, registros)
    print('¡DATOS GUARDADOS CORRECTAMENTE!')

def listar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print("No hay categorías registradas.")
    for elemento in registros:
        _imprimir_item_categoria(elemento)

def buscar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print('No hay registros para buscar.')
        
    id_buscar = validar_entero("Ingrese el id a buscar: ")
    for elemento in registros:
        if elemento.get('id') == id_buscar:
            return _imprimir_item_categoria(elemento)
    print(f'NO SE ENCONTRÓ EL ID: {id_buscar}')

def validar_categoria(id_cat):
    """Retorna el objeto categoría si existe, sino False."""
    registros = cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        if elemento.get('id') == id_cat:
            return {
                'id': elemento.get('id'),
                'categoria': elemento.get('nombre')
            }
    return False

def actualizar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print('No hay registros para actualizar.')
        
    listar_categoria()
    id_act = validar_entero("Ingrese el id a actualizar: ")
    for elemento in registros:
        if elemento.get('id') == id_act:
            op = validar_menu('\n1. Nombre Categoria\n2. Cancelar\n', 1, 2)
            if op == 1:
                elemento['nombre'] = validar_texto('Ingrese la categoria: ', 1, 20)
                guardar(NOMBRE_ARCHIVO, registros)
                print('¡DATO ACTUALIZADO!')
            else:
                print('Operación cancelada.')
            return
    print(f'NO SE ENCONTRÓ EL ID: {id_act}')

def eliminar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return print('No hay registros para eliminar.')
        
    listar_categoria()
    id_elim = validar_entero("Ingrese el id a eliminar: ")
    for elemento in registros:
        if elemento.get('id') == id_elim:
            print(f"La categoría {elemento.get('nombre')} ha sido eliminada.")
            registros.remove(elemento)
            guardar(NOMBRE_ARCHIVO, registros)
            return
    print(f'NO SE ENCONTRÓ EL ID: {id_elim}')