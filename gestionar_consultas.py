import gestionar_json as gestor
from validaciones import validar_menu, validar_entero

def stock_minimo():
    registros = gestor.cargar('herramientas.json')
    if not registros: return print('No hay registros')
    
    limite = validar_entero("Ingrese el stock mínimo: ")
    encontrados = [h for h in registros if h.get('cantidad', 0) <= limite]
    
    if encontrados:
        for h in encontrados: _imprimir_herramienta(h)
    else:
        print(f'No se encontraron herramientas con stock <= {limite}')

def activos_completados():
    registros = gestor.cargar('prestamos.json')
    if not registros: return print('No hay registros')
    
    op = validar_menu('1. En proceso\n2. Completados', 1, 2)
    filtro = ['En proceso'] if op == 1 else ['Aceptada', 'Rechazada']
    
    encontrados = [p for p in registros if p.get('estado') in filtro]
    for p in encontrados: _imprimir_prestamo(p)
    if not encontrados: print("No se encontraron registros en ese estado.")

# Optimización de Reportes (De O(N^2) a O(N))
def _obtener_top_uso(clave_entidad):
    prestamos = gestor.cargar('prestamos.json')
    conteo = {}
    for p in prestamos:
        eid = p.get(clave_entidad, {}).get('id')
        if eid: conteo[eid] = conteo.get(eid, 0) + 1
    return conteo

def herramienta_mas_usada():
    frecuencias = _obtener_top_uso('herramienta')
    herramientas = gestor.cargar('herramientas.json')
    for h in herramientas:
        if h['id'] in frecuencias:
            print(f"{h['id']}, {h['nombre']} = {frecuencias[h['id']]}")