class Departamentos:
    def __init__(self, lista):
        self.lista = lista
        self.departamentos = {}
    
    def add_departamento(self, departamento): # Añadir
        self.departamentos[departamento] = []

    def add_empleados(self, departamento, empleado):
        self.departamentos[departamento] += [empleado]
    
    def ver_departamentos(self):
        return self.departamentos

lista_departamentos = Departamentos('lista')

lista_departamentos.add_departamento('Juan Benitez')

print(lista_departamentos.departamentos)

lista_departamentos.add_empleados('Juan Benitez', 'Gustavo')

print(lista_departamentos.departamentos)

lista_departamentos.add_empleados('Juan Benitez', 'Fernando')

print(lista_departamentos.departamentos)

"""
departamentos_empleados = {'Juan Benitez' : ['Gustavo', 'Matias'],
                           'Adolfo' : ['Fernando', 'Anibal']}

print(departamentos_empleados)

for k, v in departamentos_empleados.items():
    print(k, v)
"""
