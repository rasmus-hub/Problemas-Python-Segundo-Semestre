class auto:  # Esta clase define el estado y el comportamiento de un coche

    ruedas = 4  # Atributos de clase

    def __init__(self, color, aceleracion):
        self.color = color  # Atributos de instancia
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelera(self):  # "self" es un alias de la misma clase
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):  # Estas funciones son métodos
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v


car1 = auto('verde', 10)
print(car1.color, car1.aceleracion)

auto.acelera(car1)

print(car1.velocidad)

auto.frena(car1)

print(car1.velocidad)