class Persona:
    def __init__(self, dni, nombre, apellidos):
        self.dni=dni
        self.nombre=nombre
        self.apellidos=apellidos

    def validar_dni(self):
        correcto=True
        if 