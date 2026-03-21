from cupshelpers import Printer
from Entidades.cliente import Cliente
from Entidades.vehiculo import Vehiculo
from Servicios.utils_fecha import string_a_fecha,diferecia_dias
#Ojb:vehiculo,trabajador
class Alquiler:
    cod=1    #Contador para el código de alquiler
    def __init__(self,cliente,vehiculo,fecha_inicio,fecha_fin,trabajador):

        self.cliente=cliente
        self.vehiculo=vehiculo
        self.trabajador=trabajador
        self.activo=False
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin
        self.fecha_recogida_vehiculo=None
        self.fecha_devolucion_vehiculo=None
        self._codigo='A'+str(type(self).cod)      #Código= A + el código actual del contador
        type(self).cod+=1                         #Sumamos 1 al contador
    @property
    def codigo(self):              #Convertimos el atributo código en accesible con @Property
        return self._codigo

#Función para comprobar si el alquiler está activo
    def __bool__(self):
        if self.activo:
            return True
        return False

#Cuanto cuesta un alquiler completo teniendo en cuenta el descuento
    def precio_alquiler(self):
        dias_alquiler=diferecia_dias(self.fecha_fin,self.fecha_inicio)
        precio_base=self.vehiculo.precio_d*dias_alquiler
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
    def iniciar_alquiler(self,fecha_recogida):
        if self.vehiculo.ocupado==False:
            self.vehiculo.ocupado=True
            self.activo=True
            self.cliente.puntos+=20
            self.fecha_recogida_vehiculo=string_a_fecha(fecha_recogida)
            self.cliente.vehiculos.append(self.vehiculo)
            return True
        return False

# Metodo que que ejecuta cuando el cliente devuelve el vehiculo
    def finalizar_alquiler(self,fecha_devolucion):
        fecha_devolucion=string_a_fecha(fecha_devolucion)
        if self.vehiculo.ocupado or (fecha_devolucion<self.fecha_recogida_vehiculo):#no se finalizar un alquiler una fecha anterior a la que inicio
            self.vehiculo.ocupado=False
            self.activo=False
            self.fecha_devolucion_vehiculo=fecha_devolucion
            self.cliente.vehiculos.remove(self.vehiculo)
            return True
        return False


