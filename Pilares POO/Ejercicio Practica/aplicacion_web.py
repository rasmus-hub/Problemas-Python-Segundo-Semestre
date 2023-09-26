# Relación Agregación y Composición

class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

class Cliente(Usuario):
    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)

class Administrador(Usuario):
    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)
        self.clientes = {} # nombre : contrasena
    
    def agregar_clientes(self, nombre, contrasena):
        self.clientes[nombre] = contrasena
    
    def modificar_nombre(self, nombre, nuevo_nombre):
        self.clientes[nuevo_nombre] = self.clientes.pop(nombre)

cliente1 = Usuario('Gustavo', '123')
cliente2 = Usuario('Matias', '321')
cliente3 = Usuario('Leandro', '444')

administrador = Administrador('Fernando', '090')

administrador.agregar_clientes(cliente1.nombre, cliente1.contrasena)
administrador.agregar_clientes(cliente2.nombre, cliente2.contrasena)
administrador.agregar_clientes(cliente3.nombre, cliente3.contrasena)

for cliente in administrador.clientes.items():
    print(cliente)

administrador.modificar_nombre('Gustavo', 'Hernan')

print('-----------------')

for cliente in administrador.clientes.items():
    print(cliente)
