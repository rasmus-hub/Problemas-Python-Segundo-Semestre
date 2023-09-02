def mostrar_deptos():
    i = 1
    for departamento in departamentos.departamentos:
        print(f'Departamento {i}: {departamento.nombre}')
        i += 1

def mostrar_empleados():
    i = 1
    for empleado in departamento.empleados:
        print(f'Empleado {i}: {empleado.nombre}')
        i += 1

def gestion_depto(departamento):
    opcion = None
    while opcion != 3:
        opcion = int(input(f'[ Departamento {departamento.nombre} ]'
                        '\n[1] Agregar Empleados'
                        '\n[2] Ver Empleados'
                        '\n[3] Salir'
                        '\nIngrese una opción: '))
        print('------------------------------------------------------')
        match opcion:
            case 1:
                empleado = Empleado(input('Ingrese el nombre del empleado: '))
                departamento.add_empleados(empleado)
            case 2:
                mostrar_empleados()
            case _:
                if opcion != 3:
                    print(f'La opción {opcion} no es válida')
        print('------------------------------------------------------')

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamento = None
    
class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
    
    def add_empleados(self, empleado):
        self.empleados.append(empleado)
        empleado.departamento = self

class Departamentos:
    def __init__(self, lista):
        self.lista = lista
        self.departamentos = []
    
    def add_departamentos(self, departamento): # Añadir
        self.departamentos.append(departamento)
        departamento.departamentos = self

departamentos = Departamentos('departamentos')

opcion = None
while opcion != 4:
    opcion = int(input('[ Menú Departamentos ]'
                       '\n[1] Agregar Departamentos'
                       '\n[2] Ver Departamentos'
                       '\n[3] Gestionar Departamentos'
                       '\n[4] Salir'
                       '\nIngrese una opción: ')) 
    
    print('------------------------------------------------------')
    
    match opcion:
        case 1:
            departamento = Departamento(input('Ingrese el nombre del departamento: ').title().strip())
            departamentos.add_departamentos(departamento)
        case 2:
            mostrar_deptos()
        case 3:
            mostrar_deptos()
            departamento = Departamento(input('Ingrese el nombre del departamento a elegir: ').title().strip())
            gestion_depto(departamento)
        case _:
                if opcion != 4:
                    print(f'La opción {opcion} no es válida')

    print('------------------------------------------------------')
