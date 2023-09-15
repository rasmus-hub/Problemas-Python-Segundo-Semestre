# Relación Asociación

class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Pedido:
    def __init__(self, id_pedido, monto):
        self.id_pedido = id_pedido
        self.monto = monto

# Objetos de la clase cliente

cliente1 = Cliente(1, 'Victor')
cliente2 = Cliente(2, 'Gustavo')

# Objetos de la clase pedido

pedido1 = Pedido(101, 80000)
pedido2 = Pedido(202, 50000)

# Se realiza la relación asociación

cliente1.Pedido = pedido1 # type: ignore
cliente2.Pedido = pedido2 # type: ignore

# Mostrar resultados

print(f'El cliente {cliente1.nombre} ha hecho '
      f'\nun pedido con el id {cliente1.Pedido.id_pedido}' # type: ignore
      f'\ncon un monto de ${cliente1.Pedido.monto}') # type: ignore

print(f'El cliente {cliente2.nombre} ha hecho '
      f'\nun pedido con el id {cliente2.Pedido.id_pedido}' # type: ignore
      f'\ncon un monto de ${cliente2.Pedido.monto}') # type: ignore