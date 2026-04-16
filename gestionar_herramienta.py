from gestionar_json import *
from validaciones import validar_menu, validar_entero, validar_texto
from gestionar_categoria import validar_categoria, listar_categoria
from transformaciones import transformar_estado

# Las variables globales se definen al principio del codigo y siempre en MAYUSCULAS
NOMBRE_ARCHIVO='herramientas.json'



def guardar_herramienta():
    registros=cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']=generar_id(registros)
    diccionario['nombre']=validar_texto('Ingrese el nombre: ',1,20)
    listar_categoria()
    id_categoria=validar_entero('Ingrese el id de la categoria: ')
    while(validar_categoria(id_categoria)==False):
        id_categoria=validar_entero('Error, Categoria no encontrada. Intente nuevamente: ')
    diccionario['categoria']=validar_categoria(id_categoria)
    diccionario['cantidad']= validar_entero('Selecciona la cantidad disponible de esta herramienta: ')
    estado_id=validar_menu('''
                                            Seleccion una de las 3 opciones del estado de una herramienta:
                                            1. Activa
                                            2. Fuera de servicio
                                            3. Reparación
                                            ''',1,3)
    diccionario['estado']=transformar_estado(estado_id)
    diccionario['precio']= validar_entero('Ingrese el valor que le costo la herramienta: ')
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO,registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')

def listar_herramienta():
    registros=cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        print(f'''
            ****************************
            ID:             {elemento.get('id','Clave no encontrada')}
            Nombre:         {elemento.get('nombre','Clave no encontrada')}
            Id Categoria:   {elemento.get('categoria', 'clave erronea').get('id','Clave no encontrada')}
            Categoria:      {elemento.get('categoria','clave erronea').get('categoria','Clave nombre categoria no encontrada')}
            Cantidad:       {elemento.get('cantidad','Cantidad no encontrada')}
            Estado:         {elemento.get('estado','Clave no encontrada')}
            Precio:         {elemento.get('precio','Clave no encontrada')}
            ''')

def validar_herramienta(id):
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede validar porque no hay registros')
    else:
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                return {
                            'id':           elemento.get('id', 'clave no encontrada'),
                            'nombre':       elemento.get('nombre', 'clave no encontrada'),
                            'categoria':    elemento.get('categoria', 'clave no encontrada').get('categoria','clave no encontrada'),
                            'estado':       elemento.get('estado', 'clave no encontrada'),
                            'precio':       elemento.get('precio', 'clave no encontrada'),
                            'cantidad':     elemento.get('cantidad','clave no encontrada')
                        }

def buscar_herramienta():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede buscar porque no hay registros')
    else:
        id=validar_entero("Ingrese el id a buscar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''
            ************************************************************
            ID:             {elemento.get('id','Clave no encontrada')}
            Nombre:         {elemento.get('nombre','Clave no encontrada')}
            ID Categoria:   {elemento.get('categoria', 'clave erronea').get('id','Clave no encontrada')}
            Categoria:      {elemento.get('categoria','clave erronea').get('categoria','Clave no encontrada')}
            Cantidad:       {elemento.get('cantidad','cantidad no encontrada')}
            Estado:         {elemento.get('estado','Clave no encontrada')}
            Precio:         {elemento.get('precio','Clave no encontrada')}
                    ''')
                return
        print('NO SE ENCONTRÓ EL ID: ',id)

def actualizar_herramienta():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_herramienta()
        id=validar_entero("Ingrese el id a actualizar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                op_actualizar=validar_menu('''
                                    1. Nombre.
                                    2. Categoria.
                                    3. Estado.
                                    4. Precio
                                    5. Cantidad
                                    6. Cancelar  
                                        ''',1,6)
                match op_actualizar:
                    case 1:
                        elemento['nombre']= validar_texto('Ingrese el nombre: ',1,20)
                    case 2:
                        listar_categoria()
                        id_categoria=validar_entero('Ingrese el id de la categoria: ')
                        while(validar_categoria(id_categoria)==False):
                            id_categoria=validar_entero('Error, categoria no encontrada. Intente nuevamente: ')
                        elemento['categoria']=validar_categoria(id_categoria)
                    case 3:
                        estado_id=validar_menu('''
                                        Seleccion una de las 3 opciones del estado de una herramienta:
                                        1. Activa
                                        2. Fuera de servicio
                                        3. Reparación
                                        ''',1,3)
                        elemento['estado']=transformar_estado(estado_id)
                    case 4:

                        elemento['precio']= validar_entero('Ingrese el valor que le costo la herramienta: ')
                    case 5:
                        elemento['cantidad']= validar_entero('Selecciona la cantidad disponible de esta herramienta: ')
                    case 6:
                        print('Operación cancelada!')
                guardar(NOMBRE_ARCHIVO, registros)
                print('DATO ACTUALIZADO!')
                return 
        print('NO SE ENCONTRÓ EL ID: ',id)

def eliminar_herramienta():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede actualizar porque no hay registros')
    else:
        listar_herramienta()
        id=validar_entero("Ingrese el id a eliminar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''{elemento.get('nombre','clave no encontrada')} ya no esta entre nosotros!''')
                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO,registros)
                return
        print('NO SE ENCONTRÓ EL ID: ',id)
