class Alumno:
    def __init__(self, rut, nombre, direccion, anio_nacimiento, posicion, anio_incorporacion, profesor, apoderado):
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.anio_nacimiento = anio_nacimiento
        self.posicion = posicion
        self.anio_incorporacion = anio_incorporacion
        self.profesor = profesor
        self.apoderado = apoderado
        self.goles = []
    
    def registrar_gol(self, fecha, cantidad_goles):
        self.goles.append((fecha, cantidad_goles))