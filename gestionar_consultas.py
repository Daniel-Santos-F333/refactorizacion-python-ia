from gestionar_json import cargar
from validaciones import validar_menu, validar_entero

def _imprimir_item_herramienta(h):
    cat = h.get('categoria', {})
    print(f'''
    ************************************************************
    ID:             {h.get("id", "N/A")}
    Nombre:         {h.get("nombre", "N/A")}
    Categoría:      {cat.get("categoria", "N/A")} (ID: {cat.get("id", "N/A")})
    Cantidad:       {h.get("cantidad", "0")}
    Estado:         {h.get("estado", "N/A")}
    Precio:         {h.get("precio", "0")}
    ''')

def stock_minimo():
    registros = cargar('herramientas.json')
    if not registros:
        return print('No hay herramientas registradas.')
        
    minimo = validar_entero("Ingrese el stock máximo para filtrar: ")
    encontrado = False
    for h in registros:
        if h.get('cantidad', 0) <= minimo:
            _imprimir_item_herramienta(h)
            encontrado = True
    
    if not encontrado:
        print(f'No hay herramientas con stock menor o igual a {minimo}')

def activos_completados():
    registros = cargar('prestamos.json')
    if not registros:
        return print('No hay préstamos para filtrar.')
        
    op = validar_menu('\n1. En proceso\n2. Finalizados (Aceptada/Rechazada)\n', 1, 2)
    estados_objetivo = ['En proceso'] if op == 1 else ['Aceptada', 'Rechazada']
    
    encontrado = False
    for p in registros:
        if p.get('estado') in estados_objetivo:
            # Aquí podrías llamar a la función de impresión de préstamos si la importas
            print(f"ID: {p.get('id')} - Usuario: {p.get('usuario', {}).get('nombre')} - Estado: {p.get('estado')}")
            encontrado = True
            
    if not encontrado:
        print("No se encontraron registros con ese estado.")

def herramienta_mas_usada():
    """Optimización O(n): Usa un contador de frecuencias."""
    prestamos = cargar('prestamos.json')
    if not prestamos:
        return print('No hay registros de préstamos.')
    
    conteo = {}
    for p in prestamos:
        h_id = p.get('herramienta', {}).get('id')
        h_nombre = p.get('herramienta', {}).get('nombre', 'Desconocida')
        if h_id:
            clave = f"ID: {h_id} | {h_nombre}"
            conteo[clave] = conteo.get(clave, 0) + 1
            
    print("\n--- FRECUENCIA DE USO (HERRAMIENTAS) ---")
    for tool, total in conteo.items():
        print(f"{tool} = {total} veces")

def usuario_mas_usado():
    prestamos = cargar('prestamos.json')
    if not prestamos:
        return print('No hay registros de préstamos.')
        
    conteo = {}
    for p in prestamos:
        u_id = p.get('usuario', {}).get('id')
        u_nombre = p.get('usuario', {}).get('nombre', 'Desconocido')
        if u_id:
            clave = f"ID: {u_id} | {u_nombre}"
            conteo[clave] = conteo.get(clave, 0) + 1
            
    print("\n--- FRECUENCIA DE USO (USUARIOS) ---")
    for user, total in conteo.items():
        print(f"{user} = {total} veces")