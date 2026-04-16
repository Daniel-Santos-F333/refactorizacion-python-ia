import os

def cargar_txt(nombre_archivo):
    """
    Lee el contenido de un archivo de texto de forma segura.
    Retorna una cadena vacía si el archivo no existe o está corrupto.
    """
    if not os.path.exists(nombre_archivo):
        # En lugar de imprimir error, devolvemos un estado neutro
        return ""
        
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except (IOError, OSError) as e:
        print(f"Error de lectura en {nombre_archivo}: {e}")
        return ""
    except Exception as e:
        print(f"Error inesperado al cargar TXT: {e}")
        return ""

def guardar_txt(nombre_archivo, mensaje, modo='a'):
    """
    Guarda o adjunta un mensaje en un archivo de texto.
    El parámetro 'modo' permite decidir si se sobreescribe ('w') o se adjunta ('a').
    """
    try:
        # Aseguramos que el mensaje sea string y agregamos salto de línea
        linea = f"{str(mensaje)}\n"
        
        with open(nombre_archivo, modo, encoding="utf-8") as archivo:
            archivo.write(linea)
    except (IOError, OSError) as e:
        print(f"Error de escritura en {nombre_archivo}: {e}")
    except Exception as e:
        print(f"Error crítico al guardar TXT: {e}")