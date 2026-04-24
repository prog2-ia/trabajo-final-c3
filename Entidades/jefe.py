from Entidades.trabajador import Trabajador

#
class Jefe(Trabajador):
    def __init__(self,dni:str,nombre:str,apellidos:str,telefono:int,horas:int)->None:
        super().__init__(dni,nombre,apellidos,telefono,horas)
        self.sueldo=self.calcular_sueldo()          #Sueldo basado en la función

    def calcular_sueldo(self) -> int:
        sueldo=self.horas*100
        return sueldo