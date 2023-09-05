def gestion_departamento(departamento):
    opcion = None
    while opcion != 3:
        opcion = int(input(f'[ Departamento {departamento} ]'
                        '\n[1] Agregar Empleados'
                        '\n[2] Ver Empleados'
                        '\n[3] Salir'
                        '\nIngrese una opción: '))
        
        print('----------------------------------------------------------')

        match opcion:
            case 1: # Agregar Empleados
                lista_departamentos.add_empleados(departamento, input('Ingrese nombre del empleado: ').title().strip())
            case 2:
                print(lista_departamentos.departamentos[departamento])
            case 3:
                if opcion != 3:
                    print(f'La opción {opcion} es inválida')
        
        print('----------------------------------------------------------')

class Departamentos:
    def __init__(self, lista):
        self.lista = lista
        self.departamentos = {}
    
    def add_departamento(self, departamento): # Añadir
        self.departamentos[departamento] = []

    def add_empleados(self, departamento, empleado):
        self.departamentos[departamento] += [empleado]

lista_departamentos = Departamentos('lista')

opcion = None
while opcion != 4:
    opcion = int(input('[ Menú Departamentos ]'
                       '\n[1] Agregar Departamentos'
                       '\n[2] Ver Departamentos'
                       '\n[3] Gestionar Departamentos'
                       '\n[4] Salir'
                       '\nIngrese una opción: '))
    
    print('----------------------------------------------------------')
    
    match opcion:
        case 1: # Agregar departamentos
            lista_departamentos.add_departamento(input('Ingrese nombre del departamento: ').title().strip())
        case 2:
            for departamento in lista_departamentos.departamentos:
                print(departamento)
        case 3:
            departamento = input('Ingrese el nombre del departamento: ').title().strip()
            gestion_departamento(departamento)
        case _:
            if opcion != 4:
                print(f'La opción {opcion} es inválida')
    
    print('----------------------------------------------------------')