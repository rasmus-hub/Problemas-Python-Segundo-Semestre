# Relación Agregación y Hereditaria

class Producto:
    def __init__(self, precio, descripcion):
        self.precio = precio
        self.descripcion = descripcion
        self.tienda = None

class ProductoElectronico(Producto):
    def __init__(self, garantia, precio, descripcion):
        super().__init__(precio, descripcion)
        self.garantia = garantia

class ProductoComestible(Producto):
    def __init__(self, fecha_vencimiento, precio, descripcion):
        super().__init__(precio, descripcion)
        self.fecha_vencimiento = fecha_vencimiento

class Tienda:
    def __init__(self):
        self.productos = [[], []] # electronicos, comestibles
    
    def agregar_productos(self, tipo, producto):
        if tipo == 'electronico':
            self.productos[0].append(producto)
        elif tipo == 'comestible':
            self.productos[1].append(producto)
        producto.tienda = self

# Se crean los objetos de la clase producto E.

xbox = ProductoElectronico('Con Garantía', 350000, 'Tiene juegos gays')
playstation = ProductoElectronico('Sin Garantía', 450000, 'Tiene juegos porno')

# Se crean los objetos de la clase producto C.

colacao = ProductoComestible('02-11-1997', 2100, 'Disfruta del sabor chocolate')
doritos = ProductoComestible('08-03-1980', 1700, 'Disfruta del sabor del dorito')

# Se crea el objeto de la clase tienda

tienda = Tienda()

# Se agregan los productos a la tienda

tienda.agregar_productos('electronico', xbox)
tienda.agregar_productos('electronico', playstation)
tienda.agregar_productos('comestible', colacao)
tienda.agregar_productos('comestible', doritos)

# Se recorre la tienda

for producto in tienda.productos[0]:
    print(producto.garantia, producto.precio, producto.descripcion)
print('----------------------------------------')
for producto in tienda.productos[1]:
    print(producto.fecha_vencimiento, producto.precio, producto.descripcion)
