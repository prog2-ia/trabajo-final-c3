from persona import Persona

class Trabajador(Persona):
    def __init__(self,dni,nombre,apellidos,cargo,sueldo_hora):
        super().__init__(dni,nombre,apellidos)
        self.cargo=cargo
        self.sueldo_hora=sueldo_hora
        self.ventas=0

    def aumento(self,dinero):
        self.sueldo_hora+=dinero
        print('El sueldo por hora de ',self,' ha aumentado a ',self.sueldo,'€.')

    def sueldo_semanal(self,horas):
        seuldo_s=horas*self.sueldo_hora
        return seuldo_s
