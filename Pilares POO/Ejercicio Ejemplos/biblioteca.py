class Libro:
	def __init__(self, titulo):
		self.titulo = titulo

class Biblioteca: # Relación Agregación, Asociación
	def __init__(self):
		self.libros = [ ]
		
	def agregar_libro(self, libro):
		self.libros.append(libro)

libro1 = Libro('Ñengo Flow')
libro2 = Libro('Don Quijote')
libro3 = Libro('Trilogia Cars')

# No hay una dependencia entre ambos

biblioteca = Biblioteca()

print('En la biblioteca aún no están los libros como '
	  f'{libro1.titulo}, {libro2.titulo}, {libro3.titulo}')

# Ingresamos los libros independientes en la clase biblioteca

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Recorremos la biblioteca

i = 1
for libro in biblioteca.libros:
	print(f'Libro {i}: {libro.titulo}')
	i += 1