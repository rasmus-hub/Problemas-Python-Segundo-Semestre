class Motor:
    def __init__(self, tipo_combustible, hp):
        self.tipo_combustible = tipo_combustible
        self.hp = hp


class Automovil:
    def __init__(self, marca, modelo, tipo_combustible, hp):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_combustible, hp)


# Creamos los objetos de ambas clases

motor1 = Motor('diesel', 400)

automovil1 = Automovil('toyota', 'SUV',
                       motor1.tipo_combustible, motor1.hp)

print(f'Marca: {automovil1.marca}'
      f'\nModelo: {automovil1.modelo}'
      f'\nTipo Combustible: {automovil1.motor.tipo_combustible}'
      f'\nHorsepower: {automovil1.motor.hp}')

# El automovil depende de un factor que es el motor para funcionar
