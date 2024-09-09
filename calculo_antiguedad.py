from datetime import datetime
from tarea5.registro_empleados import empleados_dict

def calcular_antiguedad(nombre):
    #calcular la antiguedad en años
    fecha_actual = datetime.now()
    fecha_ingreso = empleados_dict[nombre]['fecha_ingreso']
    antiguedad = fecha_actual.year - fecha_ingreso.year - ((fecha_actual.month, fecha_actual.day) < (fecha_ingreso.month, fecha_ingreso.day))
    return antiguedad 
