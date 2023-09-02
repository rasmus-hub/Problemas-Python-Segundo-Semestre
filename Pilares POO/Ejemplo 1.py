class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class Pedido:
    def __init__(self, id_pedido, monto):
        self.id_pedido = id_pedido
        self.monto = monto


# Crear objetos para ambas clases
# Objeto de la clase Cliente

cliente1 = Cliente(1, 'Gustavo')

cliente2 = Cliente(2, 'Matías')

# Objeto de la clase Pedido

pedido1 = Pedido(101, 800000)

# Realizamos la relación asociación entre ambas clases

cliente1.Pedido = pedido1 # La informacíon del pedido1 se almacena en cliente1

# Mostramos resultados

print(f'El cliente {cliente1.nombre} ha realizado un pedido con el id '
      f'{cliente1.Pedido.id_pedido} por un monto de ${cliente1.Pedido.monto}')

print(cliente2.id, cliente2.nombre)