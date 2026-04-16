import gestionar_json as gestor
from validaciones import validar_menu, validar_entero

# --- Utilidades de Visualización ---

def _imprimir_item_herramienta(h):
    """Estandariza la impresión de una herramienta."""
    print(f'''
            ****************************
            ID:             {h.get('id', 'N/A')}
            Nombre:         {h.get('nombre', 'N/A')}
            Id Categoria:   {h.get('categoria', {}).get('id', 'N/A')}
            Categoria:      {h.get('categoria', {}).get('categoria', 'N/A')}
            Cantidad:       {h.get('cantidad', 0)}
            Estado:         {h.get('estado', 'N/A')}
            Precio:         {h.get('precio', 0)}
            ''')

def _imprimir_item_prestamo(p):
    """Estandariza la impresión de un préstamo."""
    u = p.get('usuario', {})
    h = p.get('herramienta', {})
    print(f'''
            ****************************
            ID:             {p.get('id', 'N/A')}
            Usuario:        {u.get('nombre', 'N/A')}
            ID Usuario:     {u.get('id', 'N/A')}
            Herramienta:    {h.get('nombre', 'N/A')}
            ID Herramienta: {h.get('id', 'N/A')}
            Fecha Inicio:   {p.get('fecha_inicio', 'N/A')}
            Fecha Entrega:  {p.get('fecha_final', 'N/A')}
            Estado:         {p.get('estado', 'N/A')}
            Observaciones:  {p.get('observaciones', 'N/A')}
            ''')

# --- Funciones de Consulta ---

def stock_minimo():
    registros = gestor.cargar('herramientas.json')
    if not registros:
        print('No hay registros de herramientas.')
        return

    limite = validar_entero("Ingrese la cantidad stock mínimo: ")
    encontrado = False

    for elemento in registros:
        if elemento.get('cantidad', 0) <= limite:
            _imprimir_item_herramienta(elemento)
            encontrado = True
    
    if not encontrado:
        print(f'NO SE ENCONTRÓ NINGÚN STOCK CON CANTIDAD <= {limite}')

def activos_completados():
    registros = gestor.cargar('prestamos.json')
    if not registros:
        print('No hay registros de préstamos.')
        return

    op = validar_menu('1. En proceso\n2. Completados', 1, 2)
    
    # Definir estados a buscar según opción
    estados_busqueda = ['En proceso'] if op == 1 else ['Aceptada', 'Rechazada']
    mensaje_error = 'EN PROCESO' if op == 1 else 'COMPLETADA O RECHAZADA'
    
    encontrado = False
    for p in registros:
        if p.get('estado') in estados_busqueda:
            _imprimir_item_prestamo(p)
            encontrado = True
            
    if not encontrado:
        print(f'NO SE ENCONTRÓ NINGÚN PRÉSTAMO EN ESTADO: {mensaje_error}')

def historial_usuarios():
    registros = gestor.cargar('prestamos.json')
    if not registros:
        print('No hay registros de préstamos.')
        return

    id_usuario = validar_entero('Ingrese el id de su Usuario: ')
    encontrado = False

    for p in registros:
        if p.get('usuario', {}).get('id') == id_usuario:
            _imprimir_item_prestamo(p)
            encontrado = True
            
    if not encontrado:
        print(f"No hay historial para el usuario con ID {id_usuario}")

# --- Reportes de Uso (Optimización de Rendimiento) ---

def _contar_frecuencias(archivo_prestamos, clave_entidad):
    """Función genérica para contar usos de herramientas o usuarios."""
    prestamos = gestor.cargar(archivo_prestamos)
    conteo = {}
    for p in prestamos:
        entidad = p.get(clave_entidad, {})
        eid = entidad.get('id')
        if eid:
            conteo[eid] = conteo.get(eid, 0) + 1
    return conteo

def herramienta_mas_usada():
    frecuencias = _contar_frecuencias('prestamos.json', 'herramienta')
    herramientas = gestor.cargar('herramientas.json')
    
    if not frecuencias:
        print('No hay registros de uso en este momento.')
        return

    for h in herramientas:
        hid = h.get('id')
        if hid in frecuencias:
            print(f"{hid}, {h.get('nombre')} = {frecuencias[hid]}")

def usuario_mas_usado():
    frecuencias = _contar_frecuencias('prestamos.json', 'usuario')
    usuarios = gestor.cargar('usuarios.json')
    
    if not frecuencias:
        print('No hay registros de uso en este momento.')
        return

    for u in usuarios:
        uid = u.get('id')
        if uid in frecuencias:
            print(f"{uid}, {u.get('nombre')} {u.get('apellido')} = {frecuencias[uid]}")