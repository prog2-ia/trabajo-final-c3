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
            self.cliente.vehiculos.append(self.vehiculo)
        else:
            print('No se puede alquilar este vehiculo ya esta ocupado')