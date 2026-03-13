from cupshelpers import Printer

#Ojb:vehiculo,trabajador
class Alquiler:
    def __init__(self,cliente,vehiculo,dias_alquiler,trabajador):
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.trabajador=trabajador
        self.dias_alquiler=dias_alquiler


    def precio_alquiler(self):
        precio=(self.vehiculo.precio_d)*self.dias_alquiler
        print( f'El precio es {precio}€')
        return precio
    def puntos(self):
        puntos=self.precio_alquiler()*100
        return puntos

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


