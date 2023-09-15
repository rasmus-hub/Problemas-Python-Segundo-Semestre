class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []
    
    def agregar_jugadores(self, jugador):
        self.jugadores.append(jugador)
        jugador.equipo = self

bayern_munich = Equipo('Bayern Munich')
bvb = Equipo('BvB')

jugador1 = Jugador('Messi')
jugador2 = Jugador('Flaitiano R.')
jugador3 = Jugador('Ronaldo')

# El equipo va a seguir existiendo

print(f'El equipo {bayern_munich.nombre} no tiene jugadores')

# Se le agregan jugadores

bayern_munich.agregar_jugadores(jugador1)
bayern_munich.agregar_jugadores(jugador2)
bayern_munich.agregar_jugadores(jugador3)

# Se recorre el equipo

print(f'El equipo {bayern_munich.nombre} si tiene jugadores, son:')

for jugador in bayern_munich.jugadores:
    print(jugador.nombre)

print(f'El equipo {bvb.nombre} no tiene jugadores')

for jugador in bvb.jugadores:
    print(jugador.nombre)
