from gestionar_json import *
from gestionar_usuario import listar_usuario, validar_usuario
from validaciones import validar_entero, validar_menu
from gestionar_herramienta import listar_herramienta, validar_herramienta
from transformaciones import solicitar_fecha_inicio, gestionar, rechazar
from datetime import timedelta

NOMBRE_ARCHIVO='prestamos.json'

def guardar_prestamo():
    registros= cargar(NOMBRE_ARCHIVO)
    diccionario={}
    diccionario['id']= generar_id(registros)
    listar_usuario()
    id_usuario= validar_entero('Ingrese el id del usuario: ')
    while (validar_usuario(id_usuario)== False):
        id_usuario=validar_entero('Error, usuario no encontrada. Intente nuevamente: ')
    diccionario['usuario']=validar_usuario(id_usuario)
    listar_herramienta()
    id_herramienta= validar_entero('Ingrese el id de la herramienta: ')
    while (validar_herramienta(id_herramienta)== False):
        id_herramienta= validar_entero('Error, Herramienta no enctrada. Intente nuevamente: ')
    diccionario['herramienta']= validar_herramienta(id_herramienta)
    diccionario['cantidad']= validar_entero('Ingrese la cantidad de herramientas a solicitar: ')
    diccionario['fecha_inicio']= solicitar_fecha_inicio()
    dias=validar_entero('Ingrese la cantidad de días a usar la herramienta: ')
    diccionario['fecha_final']= diccionario.get('fecha_inicio','Clave no encontrada') + timedelta(days=dias)
    diccionario['fecha_inicio']= str(diccionario.get('fecha_inicio','fecha inicio no encontrada'))
    diccionario['fecha_final']= str(diccionario.get('fecha_final','fecha final no encontrada'))
    diccionario['estado']= 'En proceso'
    diccionario['observaciones']= 'Pendiente'
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO, registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')
    print(f'SU ID ES {diccionario.get('id', 'ID no encontrado')}, POR FAVOR GUARDELO PARA HACER SEGUIMIENTO')

def listar_prestamo():
    registros=cargar(NOMBRE_ARCHIVO)
    for elemento in registros:
        print(f'''
            ****************************
            ID:             {elemento.get('id','Clave no encontrada')}
            Usuario:        {elemento.get('usuario','Clave no encontrada').get('nombre','clave no encontrada')}
            ID Usuario:     {elemento.get('usuario', 'clave erronea').get('id','Clave no encontrada')}
            Herramienta:    {elemento.get('herramienta','clave erronea').get('nombre','Clave no encontrada')}
            ID Herramienta: {elemento.get('herramienta','Clave no encontrada').get('id','Clave no encontrada')}
            Fecha Inicio:   {elemento.get('fecha_inicio','Clave no encontrada')}
            Fecha Entrega:  {elemento.get('fecha_final','Clave no encontrada')}
            Cantidad:       {elemento.get('cantidad','Clave no encontrada')}
            Estado:         {elemento.get('estado','Clave no encontrada')}
            Observaciones:  {elemento.get('observaciones','Clave no encontrada')}
            ''')

def consultar_prestamo():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay registros en este momento')
    else:
        id_usuario=validar_entero('Ingrese el id de su Usuario. Si no lo conoce contacte al administrador: ')
        for elemento in registros:
            if elemento.get('usuario','Clave no encontrada').get('id', 'id no encontrado') == id_usuario:
                print(f'''
                    ****************************
                    ID:             {elemento.get('id','Clave no encontrada')}
                    Usuario:        {elemento.get('usuario','Clave no encontrada').get('nombre','clave no encontrada')}
                    ID Usuario:     {elemento.get('usuario', 'clave erronea').get('id','Clave no encontrada')}
                    Herramienta:    {elemento.get('herramienta','clave erronea').get('nombre','Clave no encontrada')}
                    ID Herramienta: {elemento.get('herramienta','Clave no encontrada').get('id','Clave no encontrada')}
                    Fecha Inicio:   {elemento.get('fecha_inicio','Clave no encontrada')}
                    Fecha Entrega:  {elemento.get('fecha_final','Clave no encontrada')}
                    Cantidad:       {elemento.get('cantidad','Clave cantidad no encontrada')}
                    Estado:         {elemento.get('estado','Clave no encontrada')}
                    Observaciones:  {elemento.get('observaciones','Clave no encontrada')}
                    ''')

def buscar_prestamo():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede buscar porque no hay registros')
    else:
        id=validar_entero("Ingrese el id a buscar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''
                    ****************************
                    ID:             {elemento.get('id','Clave no encontrada')}
                    Usuario:        {elemento.get('usuario','Clave no encontrada').get('nombre','clave no encontrada')}
                    ID Usuario:     {elemento.get('usuario', 'clave erronea').get('id','Clave no encontrada')}
                    Herramienta:    {elemento.get('herramienta','clave erronea').get('nombre','Clave no encontrada')}
                    ID Herramienta: {elemento.get('herramienta','Clave no encontrada').get('id','Clave no encontrada')}
                    Fecha Inicio:   {elemento.get('fecha_inicio','Clave no encontrada')}
                    Fecha Entrega:  {elemento.get('fecha_final','Clave no encontrada')}
                    Estado:         {elemento.get('estado','Clave no encontrada')}
                    Observaciones:  {elemento.get('observaciones','Clave no encontrada')}
                    ''')
                return
        print('NO SE ENCONTRÓ EL ID: ',id)

def gestionar_prestamo():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede gestionar porque no hay registros')
    else:
        listar_prestamo()
        id_prestamo=validar_entero('Ingrese el id del prestamo a gestionar: ')
        for elemento in registros:
            elemento= elemento
            if elemento.get('id','Clave no encontrada') == id_prestamo:
                op_gestionar= validar_menu('''
                                            Seleccione que opción desea realizar con el prestamo:
                                            1. Gestionar
                                            2. Rechazar
                                            ''',1,2)
                match op_gestionar:
                    case 1:
                        gestionar(elemento.get('herramienta','clave no encontrado').get('id','clave no encontrada'),elemento)
                    case 2:
                        rechazar(elemento)
                guardar(NOMBRE_ARCHIVO,registros)
                return
        print('NO SE ENCONTRÓ EL ID: ',id)
                        
def eliminar_prestamo():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No se puede eliminar porque no hay registros')
    else:
        listar_prestamo()
        id=validar_entero("Ingrese el id a eliminar: ")
        for elemento in registros:
            if elemento.get('id', 'clave no encontrada')==id:
                print(f'''{elemento.get('nombre','clave no encontrada')} ya no esta entre nosotros!''')
                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO,registros)
                return
        print('NO SE ENCONTRÓ EL ID: ',id)