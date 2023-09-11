class Persona:  # Super objeto
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut


class Estudiante(Persona):
    def __init__(self, nro_matricula, nombre, rut):
        super().__init__(nombre, rut)
        self.nro_matricula = nro_matricula
        self.asignatura = None  # Va a existir desde el momento en el que se cree la relación (asignatura: Asignatura)


class Profesor(Persona):
    def __init__(self, especialidad, nombre, rut):
        super().__init__(nombre, rut)
        self.especialidad = especialidad


class Asignatura:  # Relacion Agregación
    def __init__(self, nombre, cantidad_horas):
        self.nombre = nombre
        self.cantidad_horas = cantidad_horas
        self.estudiantes = []

    def add_estudiantes(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.asignatura = self


class Carrera:  # Relacion Composición, ya que se compone de asignaturas para funcionar
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas = []

    def add_asignaturas(self, asignatura): # Se le pasa un objeto
        self.asignaturas.append(asignatura)
        asignatura.carrera = self

# Se hace un ciclo for para agregar estudiantes de forma sucesiva

def agregar_estudiantes():
    nombre = None
    matricula = 1
    print('"Cancelar" para parar')
    while nombre != 'Cancelar':

        nombre = input('Ingrese el nombre del estudiante: ').title().strip()
        if nombre == 'Cancelar':
            break
        asignatura = int(input('[1] Intro Programacion'
                               '\n[2] Base de Datos'
                               '\n[3] Mecanica 1'
                               '\nIngrese asignatura a la que asiste (número): '))
        rut = int(input('Ingrese rut del estudiante: '))
        estudiante = Estudiante(matricula, nombre, rut)
        matricula += 1

        if asignatura == 1:
            intro_progra.add_estudiantes(estudiante)
        elif asignatura == 2:
            base_datos.add_estudiantes(estudiante)
        elif asignatura == 3:
            mecanica_uno.add_estudiantes(estudiante)
        print('----------------------------------------------------------')

# Recorrer objetos

def ver_estudiantes():
    if intro_progra.estudiantes == [] and base_datos.estudiantes == [] and mecanica_uno.estudiantes == []:
        print('No hay estudiantes registrados')
    else:
        print(f'Carrera: {carrera_mecanica.nombre}')
        for asignatura in carrera_mecanica.asignaturas:
            print(f'Asignatura: {asignatura.nombre}')
            for estudiante in asignatura.estudiantes:
                print(f'Estudiante: {estudiante.nombre}'
                    f'\nMatricula: {estudiante.nro_matricula}')
                print('----------------------------------------------------------')
            print('----------------------------------------------------------')

        print(f'Carrera: {carrera_analista_p.nombre}')
        for asignatura in carrera_analista_p.asignaturas:
            print(f'Asignatura: {asignatura.nombre}')
            for estudiante in asignatura.estudiantes:
                print(f'Estudiante: {estudiante.nombre}'
                    f'\nMatricula: {estudiante.nro_matricula}')
                print('----------------------------------------------------------')
            print('----------------------------------------------------------')

# Pueden haber relacion-composicion o solo composiciones para funcionar

# Creamos objeto del tipo Estudiante y Profesor (Relacion Heredacion)

profesor1 = Profesor('Ped. Matematicas', 'Alfonso', 117401082)

# Creamos asignaturas

intro_progra = Asignatura('Intro. a la programación', 72)
base_datos = Asignatura('Base de datos 1', 90)
mecanica_uno = Asignatura('Mecanica 1', 72)

# Relacion Composición. Creamos las carreras y agreamos asignaturas a ellas

carrera_mecanica = Carrera('Mecanica Automotriz')
carrera_analista_p = Carrera('Analista Programador')

carrera_mecanica.add_asignaturas(mecanica_uno)
carrera_analista_p.add_asignaturas(intro_progra)
carrera_analista_p.add_asignaturas(base_datos)

# Se hace un menú

opcion = None
while opcion != 3:
    opcion = int(input('[ Menú Carreras ]'
                       '\n[1] Agregar Estudiantes'
                       '\n[2] Ver estudiantes'
                       '\n[3] Salir'
                       '\nIngrese una opción: '))
    
    match opcion:
        case 1:
            agregar_estudiantes()
        case 2:
            ver_estudiantes()
        case _:
            if opcion != 3:
                print(f'La opción {opcion} no es válida')
