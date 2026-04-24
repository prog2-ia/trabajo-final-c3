from Entidades.trabajador import Trabajador

class Limpiador(Trabajador):
    def __init__(self,dni:str,nombre:str,apellidos:str,telefono:int,horas:int):
        super().__init__(dni, nombre, apellidos, telefono,horas)
        self.sueldo=self.calcular_sueldo()

    def calcular_sueldo(self) -> int:
        sueldo = self.horas * 10
        return sueldo