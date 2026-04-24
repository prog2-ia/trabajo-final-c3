

class Sede:
    def __init__(self, idSede:int, nombre:str, ciudad:str, direccion:str, telefono:int):
        self.idSede = idSede
        self.nombre = nombre
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.vehiculos = []
        self.trabajadores = []