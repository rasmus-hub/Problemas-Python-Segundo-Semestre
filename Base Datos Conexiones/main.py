from db_manager import AdministradorBaseDatos
from modelos import Producto

def close_conexion(self):
        self.conexion.close()

def main():
    base_datos = AdministradorBaseDatos('inventario.db')  # .db es la extensión de base de datos (database)

    opcion = None
    while opcion != 4:
        opcion = int(input('[ Menú Base de Datos ]'
                           '\n[1] Insertar Productos'
                           '\n[2] Obtener Productos'
                           '\n[3] Eliminar Productos'
                           '\n[4] Salir'
                           '\nIngrese la opción: '))

        match opcion:
            case 1:
                # Insertar productos en la tabla
                nombre = input('Ingrese el nombre: ')
                precio = int(input('Ingrese el precio: '))
                stock = int(input('Ingrese el stock: '))
                producto = Producto(nombre=nombre, precio=precio, stock=stock)
                print('Productos correctamente agregados')
                base_datos.insertar_productos(producto)
            case 2:
                productos = base_datos.obtener_productos()
                print('Se han encontrado los siguientes productos: ')
                for producto in productos:
                    print(producto)
            case 3:
                id_producto = input('Ingrese el id del producto a eliminar: ')
                base_datos.eliminar_productos(id_producto)
        print('--------------------------------------')
    close_conexion()

if __name__ == '__main__':
    main()
