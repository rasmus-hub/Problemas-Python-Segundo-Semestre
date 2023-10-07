# Este archivo se comunicará con los modelos

import sqlite3
from modelos import Producto


# Crear clase que controlará esa conexión

class AdministradorBaseDatos:
    def __init__(self, nombre_basedatos):
        self.conexion = sqlite3.connect(
            nombre_basedatos)  # El atributo conexion se conectará a la base de datos a través del metodo connect
        self.crear_tabla()

    def crear_tabla(self):
        try:
            cursor = self.conexion.cursor()  # Cursor es el metodo que se usa para crear query's
            query = '''
                    CREATE TABLE IF NOT EXISTS productos(
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    precio INTEGER NOT NULL,
                    stock INTEGER NOT NULL
                    )
            '''  # Consulta en la base de datos
            cursor.execute(query)  # Ejecutar una consulta
        except Exception as e:  # Se coloca exception ya que no se sabe que podria fallar
            print(f'Error al crear la tabla: {e}')
        finally:  # Finalmente pase lo que pase
            cursor.close()

    def insertar_productos(self, producto):
        try:
            cursor = self.conexion.cursor()
            query = '''
                    INSERT INTO productos(nombre, precio, stock)
                    VALUES(?, ?, ?)
            '''  # Los signos ? hacen referencia a los atributos que tendrá ese producto ya que no sabemos cuales son
            cursor.execute(query,
                           (producto.nombre, producto.precio,
                            producto.stock))
            self.conexion.commit()  # Ejecutar querys completas
        except Exception as e:
            print(f'Error al insertar el producto: {e}')
        finally:
            cursor.close()

    def obtener_productos(self):
        try:
            cursor = self.conexion.cursor()
            query = 'SELECT * FROM productos'
            cursor.execute(query)
            # Crear lista de objetos para recorrer
            productos = [Producto(id=fila[0], nombre=fila[1], precio=fila[2], stock=fila[3])
                         # 0 se refiere a la columna 0 y asi, y fila es el orden de los atributos
                         for fila in cursor.fetchall()]  # fetchall sirve para conseguir todos los atributos
        except Exception as e:
            print(f'Error al obtener productos: {e}')
        finally:
            cursor.close()
            return productos

    def eliminar_productos(self, id_producto):
        try:
            cursor = self.conexion.cursor()
            query = f'''
                    DELETE 
                    FROM productos
                    WHERE id = {id_producto}
            '''
            cursor.execute(query)
            self.conexion.commit()
        except Exception as e:
            print(f'Error al eliminar el producto: {e}')
        finally:
            cursor.close()
    # Cerrar la conexión completamente con un método
    def close_conexion(self):
        self.conexion.close()
