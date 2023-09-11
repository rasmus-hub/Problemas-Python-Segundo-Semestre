# Relación Agregación

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamento = None


class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def add_empleados(self, empleado):  # Se agregan objetos de la clase empleados
        self.empleados.append(empleado)
        empleado.departamento = self  # El departamento del empleado va a estar a cargo como objeto


# Crear objetos del tipo Empleado

nombre_empleado1 = input('Ingrese nombre empleado 1: ')
nombre_empleado2 = input('Ingrese nombre empleado 2: ')
empleado_1 = Empleado(nombre_empleado1)
empleado_2 = Empleado(nombre_empleado2)

# Crear objeto del tipo Departamento

nombre_depto = input('Ingrese nombre departamento:')
departamento = Departamento(nombre_depto)

# Agregamos empleados al departamento

departamento.add_empleados(empleado_1)
departamento.add_empleados(empleado_2)

# Acceder a los empleados que tiene el departamento

print(f'Lista de Empleados del departamento {departamento.nombre}:')

i = 1
for empleado in departamento.empleados:
    print(f'Empleado {i}: {empleado.nombre}')
    i += 1

# El departamento no dejará de ser departamento al no tener empleados
# Lo que se agrega al elemento debe crearse primero
