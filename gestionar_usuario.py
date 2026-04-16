from gestionar_json import *
from validaciones import validar_entero, validar_texto, validar_menu
from transformaciones import transformar_tipo
from gestionar_herramienta import listar_herramienta

NOMBRE_ARCHIVO= 'usuarios.json'

def guardar_usuario():
    registros=cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']=generar_id(registros)
    diccionario['nombre']= validar_texto('Ingrese el nombre de la persona: ',1,30)
    diccionario['apellido']= validar_texto('Ingrese el apellido de la persona: ',1,30)
    diccionario['telefono']= validar_entero('Ingrese su numero de telefono: ')
    diccionario['direccion']= validar_texto('Ingrese la dirección de residencia del usuario: ',1,50)
    tipo_id=validar_menu('''
                                            Seleccion el tipo de usuario:
                                            1. Residente
                                            2. Administrador
                                            ''',1,2)
    diccionario['tipo']=transformar_tipo(tipo_id)
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO,registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')

def listar_usuario():
    registros=cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        print(f'''
            ****************************
            ID:             {elemento.get('id','Clave no encontrada')}
            Nombre:         {elemento.get('nombre','Clave no encontrada')}
            Apellido:       {elemento.get('apellido', 'clave erronea')}
            Telefono:       {elemento.get('telefono','clave erronea')}
            Direccion:      {elemento.get('direccion','Clave no encontrada')}
            Tipo Usuario:   {elemento.get('tipo','Clave no encontrada')}
            ''')

def buscar_usuario():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        id=validar_entero("Ingrese el id a buscar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''
            ID:             {elemento.get('id','Clave no encontrada')}
            Nombre:         {elemento.get('nombre','Clave no encontrada')}
            Apellido:       {elemento.get('apellido', 'clave erronea')}
            Telefono:       {elemento.get('telefono','clave erronea')}
            Direccion:      {elemento.get('direccion','Clave no encontrada')}
            Tipo Usuario:   {elemento.get('tipo','Clave no encontrada')}
            ''')
                return
        print('NO SE ENCONTRÓ EL ID: ',id)

def validar_usuario(id):
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede validar porque no hay registros')
    else:
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                return {
                            'id':           elemento.get('id', 'clave no encontrada'),
                            'nombre':       elemento.get('nombre', 'clave no encontrada'),
                            'apellido':     elemento.get('apellido', 'clave no encontrada'),
                            'telefono':     elemento.get('telefono', 'clave no encontrada'),
                            'direccion':    elemento.get('direccion', 'clave no encontrada'),
                        }

def actualizar_usuario():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_usuario()
        id=validar_entero("Ingrese el id a actualizar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                op_actualizar=validar_menu('''
                                    1. Nombre.
                                    2. Apellido.
                                    3. Telefono.
                                    4. Direccion
                                    5. Tipo de usuario
                                    6. Cancelar  
                                        ''',1,5)
                match op_actualizar:
                    case 1:
                        elemento['nombre']= validar_texto('Ingrese el nombre: ',1,20)
                    case 2:
                        elemento['apellido']= validar_texto('Ingrese el nombre: ',1,20)
                    case 3:
                        elemento['telefono']= validar_entero('Ingrese su numero de telefono: ')
                    case 4:
                        elemento['direccion']= validar_texto('Ingrese la dirección de residencia del usuario: ',1,50)
                    case 5:
                        tipo_id=validar_menu('''
                                            Seleccion el tipo de usuario:
                                            1. Residente
                                            2. Administrador
                                            ''',1,2)
                        elemento['tipo']=transformar_tipo(tipo_id)
                    case 6:
                        print('Operación cancelada!')
                guardar(NOMBRE_ARCHIVO, registros)
                print('DATO ACTUALIZADO!')
                return 
        print('NO SE ENCONTRÓ EL ID: ',id)

def eliminar_usuario():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_usuario()
        id=validar_entero("Ingrese el id a eliminar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''{elemento.get('nombre','clave no encontrada')} ya no esta entre nosotros!''')
                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO,registros)
                return
        print('NO SE ENCONTRÓ EL ID: ',id)