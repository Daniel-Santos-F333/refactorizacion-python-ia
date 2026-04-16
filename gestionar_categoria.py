from validaciones import validar_menu, validar_texto, validar_entero
from gestionar_json import *


NOMBRE_ARCHIVO='categorias.json'

def guardar_categoria():
    registros=cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']=generar_id(registros)
    diccionario['nombre']=validar_texto('Ingrese la categoria de la herramienta: ',1,30)
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO,registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')

def listar_categoria():
    registros=cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        print(f'''
            *********************************************************
            id:             {elemento.get('id','clave erronea')}
            categoria:      {elemento.get('nombre','clave erronea')}
            ''')

def buscar_categoria():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede buscar porque no hay registros')
    else:
        id=validar_entero("Ingrese el id a buscar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''
                    ****************************
                    ID:             {elemento.get('id','clave erronea')}
                    Categoria:      {elemento.get('nombre','clave erronea')}
                    ''')
                return
        print('NO SE ENCONTRÓ EL ID: ',id)

def validar_categoria(id):
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede validar porque no hay registros')
    else:
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                return {
                            'id': elemento.get('id', 'clave no encontrada'),
                            'categoria': elemento.get('nombre', 'clave no encontrada')
                        }
    return False

def actualizar_categoria():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_categoria()
        id=validar_entero("Ingrese el id a actualizar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                op_actualizar=validar_menu('''
                                    1. Nombre Categoria.
                                    2. Cancelar   
                                        ''',1,2)
                match op_actualizar:
                    case 1:
                        elemento['nombre']=validar_texto('Ingrese la categoria: ',1,20)
                    case 2:
                        print('Operación cancelada!')
                guardar(NOMBRE_ARCHIVO, registros)
                print('DATO ACTUALIZADO!')
                return 
        print('NO SE ENCONTRÓ EL ID: ',id)

def eliminar_categoria():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede eliminar porque no hay registros')
    else:
        listar_categoria()
        id=validar_entero("Ingrese el id a eliminar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''{elemento.get('categoria','clave no encontrada')} ya no esta entre nosotros!''')
                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO,registros)
                return
        print('NO SE ENCONTRÓ EL ID: ',id)