import os
import json

def cargar_txt(nombre_archivo):
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                return archivo.read()
        else:
            return ""
    except Exception as e:
        print(f'{e}, Hay un error en la funcion de cargar txt')

def guardar_txt(nombre_archivo, mensaje):
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")
