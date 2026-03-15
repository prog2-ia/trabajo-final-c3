from cupshelpers import Printer

from Entidades.cliente import Cliente
from Entidades.vehiculo import Vehiculo


#Ojb:vehiculo,trabajador
class Alquiler:
    def __init__(self,cliente,vehiculo,dias_alquiler,trabajador):
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.trabajador=trabajador
        self.dias_alquiler=dias_alquiler
        self.activo=False
        self.fecha_inicio=None
        self.fecha_fin=None

#Cuanto cuesta un alquiler completo teniendo en cuenta el decuento
    def precio_alquiler(self):
        precio_base=self.vehiculo.precio_d*self.dias_alquiler
        descuento=0

        if self.dias_alquiler>=14:
            descuento=0.1
        elif self.dias_alquiler>=7:
            descuento=0.05

        if self.cliente.puntos>=100:
            self.cliente.puntos-=25
            descuento+=0.1

        return precio_base*(1-descuento)

#Metodo que que ejecuta cuando el cliente recoge el vehiculo
    def iniciar_alquiler(self,fecha_inicial):
        if self.vehiculo.ocupado==False:
            self.vehiculo.ocupado=True
            self.activo=True
            self.cliente.puntos+=20
            self.fecha_inicio=fecha_inicial
            self.cliente.vehiculos.append(self.vehiculo)

# Metodo que que ejecuta cuando el cliente devuelve el vehiculo
    def finalizar_alquiler(self, fecha_fin):
        if self.vehiculo.ocupado:
            self.vehiculo.ocupado=False
            self.activo=False
            self.fecha_inicio=fecha_fin
            self.cliente.vehiculos.remove(self.vehiculo)

