class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tienda = None

class Tienda:
    def __init__(self):
        self.productos = []
    
    def agregar_productos(self, producto):
        self.productos.append(producto)
        producto.tienda = self

tienda = Tienda()

producto1 = Producto('Cereales Trix')
producto2 = Producto('Mantecol')
producto3 = Producto('Lays')

tienda.agregar_productos(producto1)
tienda.agregar_productos(producto2)
tienda.agregar_productos(producto3)

i = 1
for producto in tienda.productos:
    print(f'Producto {i}: {producto.nombre}')
    i += 1