from gestionar_json import *
from validaciones import validar_menu, validar_entero
from gestionar_herramienta import listar_herramienta

def stock_minimo():
    registros=cargar('herramientas.json')
    if not registros:
        print('No se puede buscar porque no hay registros')
    else:
        stock=validar_entero("Ingrese la cantidad stock minimo que se encuentre disponible en las herramientas que desea buscar: ")
        for elemento in registros:
            if elemento.get('cantidad', 'clave no encontrada') <= stock:
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
                return
        print('NO SE ENCONTRÓ NINGÚN STOCK CON ESA CANTIDAD MINIMA: ',stock)

def activos_completados():
    registros=cargar('prestamos.json')
    if not registros:
        print('No se puede buscar porque no hay registros')
    else:
        op= validar_menu('''
                        1. En proceso
                        2. Completados
                        ''',1,2)
        match op:
            case 1:
                for elemento in registros:
                    if elemento.get('estado', 'clave no encontrada')=='En proceso':
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
                    else:
                        print('NO SE ENCONTRO NINGUN PRESTAMO EN ESTADO DE: EN PROCESO')
            case 2:
                for elemento in registros:
                    if elemento.get('estado', 'clave no encontrada')=='Aceptada' or elemento.get('estado', 'clave no encontrada')=='Rechazada':
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
                        
                    else:
                        print('NO SE ENCONTRÓ NINGUN PRESTAAMO EN ESTADO: COMPLETADA O RECHAZADA')

def historial_usuarios():
    registros=cargar('prestamos.json')
    if not registros:
        print('No hay registros en este momento')
    else:
        id_usuario=validar_entero('Ingrese el id de su Usuario. Si no lo conoce contacte al administrador: ')
        for elemento in registros:
            if elemento.get('usuario','Clave no encontrada').get('id','id de usuario no encontrado') == id_usuario:
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

def herramienta_mas_usada():
    herramientas_list=cargar('herramientas.json')
    resultados=[]
    contador=0
    registros= cargar('prestamos.json')
    if not registros:
        print('No hay registros en este momento')
    else:
        for i_herramientas in herramientas_list:
            contador=0
            for i_prestamos in registros:
                if i_herramientas['id']==i_prestamos['herramienta']['id']:
                    contador+=1
            if contador>0:
                resultados.append(f'{i_herramientas['id']}, {i_herramientas['nombre']} = {contador}\n')
    print(*resultados, sep="")

def usuario_mas_usado():
    usuarios_list=cargar('usuarios.json')
    resultados=[]
    contador=0
    registros= cargar('prestamos.json')
    if not registros:
        print('No hay registros en este momento')
    else:
        for i_usuario in usuarios_list:
            contador=0
            for i_prestamos in registros:
                if i_usuario['id']==i_prestamos['usuario']['id']:
                    contador+=1
            if contador>0:
                resultados.append(f'{i_usuario['id']}, {i_usuario['nombre']} {i_usuario['apellido']} = {contador}\n')
    print(*resultados, sep="")
        





