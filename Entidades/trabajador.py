from abc import ABC, abstractmethod

from Entidades.persona import Persona
#Hereda persona
class Trabajador(Persona,ABC):
    def __init__(self,dni,nombre,apellidos,telefono,sueldo):
        super().__init__(dni,nombre,apellidos,telefono)
        self.sueldo=sueldo
        self.ventas=0

    #@abstractmethod
    #def calcular_salario(self):
    #    pass

    def aumento(self,dinero):
        self.sueldo+=dinero
        print('El sueldo de ',self,' ha aumentado a ',self.sueldo,'€.')