from gestionar_txt import *
from datetime import datetime


def historial(mensaje):
    fecha= str(datetime.now())
    accion = mensaje + ' en la fecha de ' + fecha
    print(accion)
    guardar_txt('historial.txt', accion)


