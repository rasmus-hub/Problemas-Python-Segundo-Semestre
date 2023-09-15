class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

class Clientes(Usuario):
    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)
    
    def modificar_nombre(self, nombre):
        self.nombre = nombre

class Administradores(Usuario):
    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)

    def modificar_nombre(self, nombre):
        Clientes.nombre = nombre # type: ignore

gustavo = Clientes('Gustavo', 'esnupi12')
matias = Clientes('Matias', 'ulises167')

administrador1 = Administradores('Alfredo', 'hualpen1973')
