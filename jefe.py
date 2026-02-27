from trabajador import Trabajador


class Jefe(Trabajador):
    def __init__(self,dni,nombre,apellidos,sueldo):
        super().__init__(dni,nombre,apellidos,sueldo)

    def despedir(self,dni):
        pass

    def aumento(self,dni,dinero):
        self.sueldo+=dinero
        print('El sueldo de ',dni,' ha aumentado a ',self.sueldo,'€.')