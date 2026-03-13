from cupshelpers import Printer

#Ojb:vehiculo,trabajador
class Alquiler:
    def __init__(self,cliente,vehiculo,dias_alquiler,trabajador):
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.trabajador=trabajador
        self.dias_alquiler=dias_alquiler


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

    def crear_reserva(self):
        if self.vehiculo.ocupado==False:
            if self.cliente.metodo_pago != []:
                self.cliente.vehiculos.append(self.vehiculo)
                self.cliente.puntos+=self.puntos()
                return True
            else:
                print('El cliente aun no tiene ningun metodo de pago')
                return False
        else:
            print('No se puede alquilar este vehiculo ya esta ocupado')
            return False


