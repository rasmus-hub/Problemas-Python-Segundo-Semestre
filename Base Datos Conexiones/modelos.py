# Creación de tablas a través de clases

class Producto:
    def __init__(self, id=None, nombre='', precio=0,stock=0):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):  # Utilizado para imprimir la información del objeto
        return (f'Producto: {self.id} | Nombre: {self.nombre} | '
                f'Precio: {self.precio} | Stock: {self.stock}')
