# Relación Agregación

class Vuelo:
    def __init__(self, num_vuelos):
        self.num_vuelos = num_vuelos
    
class Aeropuerto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelos = []
    
    def agregar_vuelos(self, vuelo):
        self.vuelos.append(vuelo)
        vuelo.aeropuerto = self

# Se crean objetos de la clase vuelo

vuelo1 = Vuelo(101)
vuelo2 = Vuelo(303)
vuelo3 = Vuelo(404)
vuelo4 = Vuelo(505)

# Se crean objetos de la clase vuelo

aeropuerto1 = Aeropuerto('Puerto Montt')
aeropuerto2 = Aeropuerto('Santiago')

# Se agregan vuelos al objeto aeropuerto

aeropuerto1.agregar_vuelos(vuelo1)
aeropuerto1.agregar_vuelos(vuelo2)
aeropuerto2.agregar_vuelos(vuelo3)
aeropuerto2.agregar_vuelos(vuelo4)

# Se recorren los datos de los dos aeropuertos

print('Vuelos del aeropuerto 1: ')

for vuelo in aeropuerto1.vuelos:
    print(vuelo.num_vuelos)

print('Vuelos del aeropuerto 2: ')

for vuelo in aeropuerto2.vuelos:
    print(vuelo.num_vuelos)