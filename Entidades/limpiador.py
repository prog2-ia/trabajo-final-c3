

from trabajador import Trabajador

class Limpiador(Trabajador):
    def __init__(self,dni,nombre,apellidos,telefono):
        super().__init__(dni, nombre, apellidos, telefono)
        self.sueldo=self.calcular_sueldo()

    def calcular_sueldo(self):
        sueldo = self.horas * 10
        return sueldo

