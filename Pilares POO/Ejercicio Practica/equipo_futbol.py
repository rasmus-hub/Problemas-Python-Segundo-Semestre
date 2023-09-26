# Relación Agregación

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self):
        self.jugadores = []
    
    def agregar_jugadores(self, jugador):
        self.jugadores.append(jugador)
        jugador.equipo = self

# Se crean objetos de la clase jugador

alexis = Jugador('Alexis S.')
matias = Jugador('Matias B.')
francisco = Jugador('Francisco N.')

# Se crea objeto de la clase equipo

equipo_futbol = Equipo()

# Se verifica si el equipo es apto para jugar

if len(equipo_futbol.jugadores) == 0:
    print('El equipo no tiene jugadores')
else:
    print('El equipo si tiene jugadores')

# Se introducen jugadores en el equipo

equipo_futbol.agregar_jugadores(alexis)
equipo_futbol.agregar_jugadores(matias)
equipo_futbol.agregar_jugadores(francisco)

# Se verifica si el equipo es apto para jugar por segunda vez

if len(equipo_futbol.jugadores) == 0:
    print('El equipo no tiene jugadores')
else:
    print('El equipo si tiene jugadores')

# Se recorre el equipo

for jugador in equipo_futbol.jugadores:
    print(jugador.nombre)