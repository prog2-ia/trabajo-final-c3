from trabajador import Trabajador

#
class Jefe(Trabajador):
    def __init__(self,dni,nombre,apellidos,telefono,horas):
        super().__init__(dni,nombre,apellidos,telefono,horas)
        self.sueldo=self.calcular_sueldo()
    def despedir(self,dni):
        pass
    def calcular_sueldo(self):
        sueldo=self.horas*100
        return sueldo
    def aumento(self,dni,dinero):
        self.sueldo+=dinero
        print('El sueldo de ',dni,' ha aumentado a ',self.sueldo,'€.')

