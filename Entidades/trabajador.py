from abc import ABC, abstractmethod

from Entidades.persona import Persona
#Hereda persona
class Trabajador(Persona,ABC):
    def __init__(self,dni,nombre,apellidos,telefono,horas):
        super().__init__(dni,nombre,apellidos,telefono)
        self.horas=horas


    @abstractmethod
    def calcular_sueldo(self, horas):
        pass

    def aumento(self,dinero):
        self.sueldo+=dinero
        print('El sueldo de ',self,' ha aumentado a ',self.sueldo,'€.')
