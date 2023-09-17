"""
En una aplicación web, hay diferentes tipos de usuario: Administradores y Clientes. 
Todos los usuarios tienen un nombre de usuario, una contraseña y la capacidad de 
iniciar sesión. Los administradores tienen la capacidad adicional de modificar configuraciones. 
Realice el código y el diagrama de clases para esta relación.
"""

import os

def limpiar_consola():
    input()
    os.system('cls')

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
    
    def cambiar_nombre(self, nombre, nuevo_nombre):
        for lista in base_datos.usuarios:
            for n, c in lista.items():
                if n == nombre:
                    base_datos.usuarios[0][nuevo_nombre] = base_datos.usuarios[0].pop(nombre)
        
class BaseDatos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = [{},{}] # Clientes, Administradores
    
    def agregar_usuarios(self, rol, nombre, contrasena):
        if rol == 'Cliente':
            self.usuarios[0][nombre] = contrasena
        elif rol == 'Administrador':
            self.usuarios[1][nombre] = contrasena

def menu_administrador(nombre_usuario):
    opcion = None
    print(f'¡Bienvenido {nombre_usuario}!')
    while opcion != 5:
        opcion = int(input('[ Menú Usuario ]'
                           '\n[1] Ver Clientes'
                           '\n[2] Ver Administradores'
                           '\n[3] Cambiar nombre de usuarios'
                           '\n[4] Cambiar contraseña de usuarios'
                           '\n[5] Salir'
                           '\nElija una opción: '))

        match opcion:
            case 1:
                i = 1
                for n, c in base_datos.usuarios[0].items():
                    print(f'Cliente {i}: {n}')
                    i += 1
            case 2:
                i = 1
                for n, c in base_datos.usuarios[1].items():
                    print(f'Cliente {i}: {n}')
                    i += 1
            case 3:
                nombre = input('Ingrese el nombre del cliente: ')
                nombre_nuevo = input('Ingrese el nombre nuevo: ')
                nombre_usuario.cambiar_nombre(nombre, nombre_nuevo)
            case _:
                if opcion != 3:
                    print(f'La opción {opcion} es inválida')
        
        limpiar_consola()

def menu_cliente(nombre_usuario):
    opcion = None
    print(f'¡Bienvenido {nombre_usuario}!')
    while opcion != 3:
        opcion = int(input('[ Menú Usuario ]'
                           '\n[1] Ver Clientes'
                           '\n[2] Ver Administradores'
                           '\n[3] Salir'
                           '\nElija una opción: '))
        match opcion:
            case 1:
                i = 1
                for n, c in base_datos.usuarios[0].items():
                    print(f'Cliente {i}: {n}')
                    i += 1
            case 2:
                i = 1
                for n, c in base_datos.usuarios[1].items():
                    print(f'Cliente {i}: {n}')
                    i += 1
            case _:
                if opcion != 3:
                    print(f'La opción {opcion} es inválida')
        
        limpiar_consola()

# Creamos los objetos de la clase administrador

base_datos = BaseDatos('base_datos')

# Creamos los objetos de la clase cliente

Matias = Cliente('Matias', '123321')
Bastian = Cliente('Bastian', '321123')

# Creamos los objetos de la clase administrador

Gustavo = Administrador('Gustavo', 'Esnupi12')
Alfredo = Administrador('Alfredo', '12Olava')

# Añadimos a los usuarios creados a la base de datos

base_datos.agregar_usuarios('Cliente', cliente1.nombre, cliente1.contrasena)
base_datos.agregar_usuarios('Cliente', cliente2.nombre, cliente2.contrasena)
base_datos.agregar_usuarios('Administrador', administrador1.nombre, administrador1.contrasena)
base_datos.agregar_usuarios('Administrador', administrador2.nombre, administrador2.contrasena)

# Inicio de sesión

nombre_usuario = input('[ Inicie Sesión ]\nNombre de Usuario: ')
contrasena_usuario = input('Contraseña: ')

for n, c in base_datos.usuarios[0].items():
    if nombre_usuario == n and contrasena_usuario == c:
        menu_cliente(nombre_usuario)
for n, c in base_datos.usuarios[1].items():
    if nombre_usuario == n and contrasena_usuario == c:
        menu_administrador(nombre_usuario)
