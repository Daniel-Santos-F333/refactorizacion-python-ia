import gestionar_json as gestor
from validaciones import *
from gestionar_categoria import validar_categoria, listar_categoria
from transformaciones import transformar_estado

FILENAME = 'herramientas.json'

def _buscar_herramienta_obj(registros, id_buscado):
    return next((h for h in registros if h.get('id') == id_buscado), None)

def guardar_herramienta():
    registros = gestor.cargar(FILENAME)
    listar_categoria()
    id_cat = validar_entero('ID Categoría: ')
    while not validar_categoria(id_cat):
        id_cat = validar_entero('Error. Reintente ID Categoría: ')
        
    nuevo = {
        'id': gestor.generar_id(registros),
        'nombre': validar_texto('Nombre: ', 1, 20),
        'categoria': validar_categoria(id_cat),
        'cantidad': validar_entero('Cantidad: '),
        'estado': transformar_estado(validar_menu('1. Activa\n2. Fuera\n3. Reparación', 1, 3)),
        'precio': validar_entero('Precio: ')
    }
    registros.append(nuevo)
    gestor.guardar(FILENAME, registros)
    print('GUARDADO EXITOSO')

def actualizar_herramienta():
    registros = gestor.cargar(FILENAME)
    if not registros: return print('Sin datos')
    
    id_act = validar_entero("ID a actualizar: ")
    h = _buscar_herramienta_obj(registros, id_act)
    if not h: return print('No encontrado')

    op = validar_menu('1.Nombre 2.Cat 3.Estado 4.Precio 5.Cant 6.Cancelar', 1, 6)
    if op == 6: return print('Cancelado')
    
    if op == 1: h['nombre'] = validar_texto('Nuevo nombre: ', 1, 20)
    elif op == 2: 
        listar_categoria()
        h['categoria'] = validar_categoria(validar_entero('Nueva Cat: '))
    elif op == 3: h['estado'] = transformar_estado(validar_menu('1..3', 1, 3))
    elif op == 4: h['precio'] = validar_entero('Precio: ')
    elif op == 5: h['cantidad'] = validar_entero('Cantidad: ')

    gestor.guardar(FILENAME, registros)
    print('ACTUALIZADO')