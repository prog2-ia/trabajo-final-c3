from Entidades.trabajador import Trabajador

#
class Jefe(Trabajador):
    def __init__(self,dni,nombre,apellidos,telefono,horas):
        super().__init__(dni,nombre,apellidos,telefono,horas)
        self.sueldo=self.calcular_sueldo()          #Sueldo basado en la función

    def calcular_sueldo(self):
        sueldo=self.horas*100
        return sueldo

