

class Sede:
    def __init__(self, idSede, nombre, ciudad, direccion, telefono):
        self.idSede = idSede
        self.nombre = nombre
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.vehiculos = []
        self.trabajadores = []