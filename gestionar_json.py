import os
import json

def cargar(nombre_archivo):
    """Carga datos desde un JSON. Si hay error o no existe, retorna lista vacía."""
    if not os.path.exists(nombre_archivo):
        return []
        
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error crítico al leer {nombre_archivo}: {e}")
        # Retornamos lista vacía para que el programa pueda seguir operando
        return []

def guardar(nombre_archivo, lista_datos):
    """Guarda la lista de datos en el JSON con formato indentado."""
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(lista_datos, archivo, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error de escritura en {nombre_archivo}: {e}")

def generar_id(datos):
    """Genera un nuevo ID basado en el valor máximo actual (más seguro)."""
    if not datos:
        return 1
    
    # Extraemos todos los IDs válidos y buscamos el máximo
    # Esto evita errores si el último elemento no tiene ID o la lista está desordenada
    ids = [item.get("id") for item in datos if isinstance(item.get("id"), int)]
    
    return max(ids) + 1 if ids else 1