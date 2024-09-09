#registro_empleados.py
from datetime import datetime

#Diccionario para almacenar la información de los empleados 
empleados_dict = {}

def agregar_empleado(nombre, salario, fecha_ingreso):
    #Añadir un nuevo empleado al diccionario 
    empleados_dict[nombre] = {'salario': float(salario), 'fecha_ingreso': fecha_ingreso}
    