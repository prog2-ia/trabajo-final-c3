from cupshelpers import Printer


class Alquiler:
    def __init__(self,cliente,vehiculo,dias_alquiler,trabajador):
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.trabajador=trabajador
        self.dias_alquiler=dias_alquiler


    def precio_alquiler(self):
        precio=(self.vehiculo.precio_d)*self.dias_alquiler
        return f'El precio es {precio}€'

    def crear_reserva(self):
        if self.vehiculo.ocupado==False:
            if self.cliente.metodo_pago != []:
                self.cliente.vehiculos.append(self.vehiculo)
                return True
            else:
                print('El cliente aun no tiene ningun metodo de pago')
                return False
        else:
            print('No se puede alquilar este vehiculo ya esta ocupado')
            return False