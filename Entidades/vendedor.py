

from trabajador import Trabajador

class Vendedor(Trabajador):
    def __init__(self,dni,nombre,apellidos,telefono,horas):
        super().__init__(dni, nombre, apellidos, telefono,horas)
        self.alquileres=[]
        self.sueldo=self.calcular_sueldo()

    def calcular_sueldo(self):
        sueldo=self.horas*15
        return sueldo
    def numero_alquileres(self):
        numero=len(self.alquileres)
        return numero

t1=Vendedor('2342','32f','afs','2423',522)
print(t1.sueldo)