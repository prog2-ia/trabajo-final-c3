from abc import ABC, abstractmethod

from Entidades.persona import Persona
#Hereda persona
class Trabajador(Persona,ABC):
    def __init__(self,dni:str,nombre:str,apellidos:str,telefono:int,horas:int)-> None:
        super().__init__(dni,nombre,apellidos,telefono)
        self.horas: int =horas
        self.sueldo:int = 0

#Creamos el abstractmethod calcular sueldo para todos los tipos de trabajadores
    @abstractmethod
    def calcular_sueldo(self, horas:int)->int:
        pass

    def aumento(self,dinero:int) -> bool:
        if dinero>0:
            self.sueldo+=dinero
            return True
        else:
            return False