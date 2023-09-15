"""
En una aplicación web, hay diferentes tipos de usuario: Administradores y Clientes. 
Todos los usuarios tienen un nombre de usuario, una contraseña y la capacidad de 
iniciar sesión. Los administradores tienen la capacidad adicional de modificar configuraciones. 
Realice el código y el diagrama de clases para esta relación.
"""

import os

def limpiar_consola():
    os.system('cls')

class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena
        self.usuarios = {}
    
    def agregar_usuarios(self, nombre, contrasena):
        self.usuarios[nombre] = contrasena

class Cliente(Usuario):
    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)

class Administrador(Usuario):
    def __init__(self, nombre, contrasena):
        super().__init__(nombre, contrasena)
        self.clientes = {}

    def modificar_nombre(self, cliente, nuevo_nombre):
        self.clientes[nuevo_nombre] = self.clientes.pop(cliente)

# Creamos los objetos de la clase administrador

base_datos = Usuario('base_datos', 'base_datos')

# Creamos los objetos de la clase cliente

cliente1 = Cliente('Matias', '123321')
cliente2 = Cliente('Bastian', '321123')

# Creamos los objetos de la clase administrador

administrador1 = Administrador('Gustavo', 'Esnupi12')
administrador2 = Administrador('Alfredo', '12Olava')

# Añadimos a los usuarios creados a la base de datos

base_datos.agregar_usuarios(cliente1.nombre, cliente1.contrasena)
base_datos.agregar_usuarios(cliente2.nombre, cliente2.contrasena)
base_datos.agregar_usuarios(administrador1.nombre, administrador1.contrasena)
base_datos.agregar_usuarios(administrador2.nombre, administrador2.contrasena)

opcion = None

nombre_usuario = input('[ Inicie Sesión ]\nNombre de Usuario: ')
contrasena_usuario = input('Contraseña: ')

for nombre, contrasena in base_datos.usuarios.items():
    if nombre_usuario == nombre and contrasena_usuario == contrasena:
        print(nombre, contrasena)
