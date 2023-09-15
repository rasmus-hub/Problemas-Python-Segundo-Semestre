class Aeropuerto:
    def __init__(self):
        self.vuelos = []
    
    def agregar_vuelos(self, vuelo):
        self.vuelos.append(vuelo)
        vuelo.aeropuerto = self
    
    def eliminar_vuelos(self, vuelo):
        self.vuelos.remove(vuelo)

class Vuelo:
    def __init__(self, num_vuelos):
        self.num_vuelos = num_vuelos

# Creamos objetos de la clase vuelo

aeropuerto = Aeropuerto()

try:
    opcion = None
    while opcion != 4:
        opcion = int(input('[ Menú Aeropuerto ]'
                        '\n[1] Agregar vuelos'
                        '\n[2] Eliminar vuelos'
                        '\n[3] Ver vuelos'
                        '\n[4] Salir'
                        '\nIngrese una opción: '))
        
        print('--------------------------------------------')
        
        match opcion:
            case 1: # Introducimos los objetos a la clase aeropuerto
                vuelo = Vuelo(int(input('Ingrese el número de vuelo: ')))
                aeropuerto.agregar_vuelos(vuelo)
            case 2: # Eliminamos los objetos a la clase aeropuerto
                if aeropuerto.vuelos == []:
                    print('El aeropuerto no tiene vuelos registrados')
                else:
                    vuelo1 = int(input('Ingrese el número de vuelo: '))
                    for vuelo in aeropuerto.vuelos:
                        if vuelo.num_vuelos == vuelo1:
                            aeropuerto.eliminar_vuelos(vuelo)
            case 3: # Verificamos y revisamos los objetos a la clase aeropuerto
                if aeropuerto.vuelos == []:
                    print('El aeropuerto no tiene vuelos registrados')
                else:
                    i = 1
                    for vuelo in aeropuerto.vuelos:
                        print(f'Vuelo {i}: {vuelo.num_vuelos}')
                        i += 1
        
        print('--------------------------------------------')

except ValueError:
    print('Valor Inválido')
