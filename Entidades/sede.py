

class Sede:
    ids_sedes = []

    def __init__(self, idSede, nombre, ciudad, direccion, telefono):
        self.idSede = idSede
        self.nombre = nombre
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.vehiculos = []
        self.empleados = []
        type(self).ids_sedes.append(idSede)


