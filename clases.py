class Vehiculo:
    def __init__(self,matricula,marca,modelo,color,deposito,tipo):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.km_recorridos=0
        self.gasolina=0
        self.deposito=deposito
        self.tipo=tipo

    def suma_km(self,km):
        self.km_recorridos+=km


    def echar_gasolina(self,gasolina):
        if self.tipo=='eléctrico':
            print('El coche ha explotado')
            del self
        else:
            if self.gasolina+gasolina<=self.deposito:
                self.gasolina+=gasolina
            else:
                print("No se puede hechar gasolina por encima del limite")
                self.gasolina=self.deposito


class Persona:
    def __init__(self,DNI,nombre,apellido,coche):
        self.dni=DNI
        self.nombre=nombre
        self.apellido=apellido
        self.coche=coche

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
