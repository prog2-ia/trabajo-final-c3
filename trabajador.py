class Trabajador:
    def __init__(self,dni,nombre,apellidos,cargo,sueldo):
        self.dni=dni
        self.apellidos=apellidos
        self.cargo=cargo
        self.sueldo=sueldo
        self.ventas=0

    def aumento(self,dinero):
        self.sueldo+=dinero
        print('El sueldo de ',self,' ha aumentado a ',self.sueldo,'€.')