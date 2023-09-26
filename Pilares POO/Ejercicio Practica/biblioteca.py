# Relación Agregación

class Libro:
	def __init__(self, titulo):
		self.titulo = titulo

class Biblioteca:
	def __init__(self):
		self.libros = [ ]
    
	def agregar_libro(self, libro):
		self.libros.append(libro)

# Se crean objetos de la clase libro

libro1 = Libro('Don Ramón')
libro2 = Libro('Rene Puente')
libro3 = Libro('Biografía de Matías Bastias')

# Se crea objeto de la clase biblioteca

biblioteca = Biblioteca()

# Se verifica que los objetos pueden existir de forma independiente

print(f'Los libros que no están en la biblioteca son: '
      f'\n{libro1.titulo}\n{libro2.titulo}\n{libro3.titulo}')

""" Se puede observar que los objetos existen sin pertenecer
a un objeto (biblioteca) """

# Se introducen los libros en la biblioteca

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Se recorre la biblioteca

print('La biblioteca tiene estos libros: ')

for libro in biblioteca.libros:
    print(libro.titulo) # Ahora los libros están dentro de la biblioteca