from persona import Persona

class Trabajador(Persona):
    def __init__(self,dni,nombre,apellidos,sueldo):
        super().__init__(dni,nombre,apellidos)
        self.cargo=cargo
        self.sueldo=sueldo
        self.ventas=0

    def aumento(self,dinero):
        self.sueldo+=dinero
        print('El sueldo de ',self,' ha aumentado a ',self.sueldo,'€.')