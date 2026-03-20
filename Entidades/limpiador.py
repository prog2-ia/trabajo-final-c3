from Entidades.trabajador import Trabajador

class Limpiador(Trabajador):
    def __init__(self,dni,nombre,apellidos,telefono,horas):
        super().__init__(dni, nombre, apellidos, telefono,horas)
        self.sueldo=self.calcular_sueldo()

    def calcular_sueldo(self):
        sueldo = self.horas * 10
        return sueldo