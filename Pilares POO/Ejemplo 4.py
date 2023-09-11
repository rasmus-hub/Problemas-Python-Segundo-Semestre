# Herencia o generalización

class Vehiculo: # Clase super()
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year


class Motocicleta(Vehiculo):  # En esta línea se realiza la herencia
    def __init__(self, cilindrada, marca, modelo, year):
        super().__init__(marca, modelo, year)  # Método super
        self.cilindrada = cilindrada


# Creamos objeto del tipo Motocicleta
moto_f1 = Motocicleta(2300, 'Yamaha', 'y1', 2021)

print(f'Cilindrada: {moto_f1.cilindrada}'
      f'\nMarca: {moto_f1.marca}'
      f'\nModelo: {moto_f1.modelo}'
      f'\nAño: {moto_f1.year}')
