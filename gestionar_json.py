import os
import json

def cargar(nombre_archivo):
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r") as archivo:
                return json.load(archivo)
        else:
            return []
    except json.JSONDecodeError as ex:
        print(ex)
        
def guardar(nombre_archivo, lista_datos):
    with open(nombre_archivo, "w") as archivo:
        json.dump(lista_datos, archivo, indent=4)

def generar_id(datos):
    if not datos:
        return 1
    return datos[-1].get("id", "error, id no encontrado")+1