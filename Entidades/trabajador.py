from abc import ABC, abstractmethod

from persona import Persona
#Hereda persona
class Trabajador(Persona,ABC):
    def __init__(self,dni,nombre,apellidos,sueldo):
        super().__init__(dni,nombre,apellidos)
        self.cargo=cargo
        self.sueldo=sueldo
        self.ventas=0

    @abstractmethod
    def calcular_salario(self):
        pass

    def aumento(self,dinero):
        self.sueldo+=dinero
        print('El sueldo de ',self,' ha aumentado a ',self.sueldo,'€.')