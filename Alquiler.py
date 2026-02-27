class Alquiler:
    def __init__(self,cliente,vehiculo,dias_alquiler,trabajador):
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.trabajador=trabajador
        self.dias_alquiler=dias_alquiler
        self.cliente.vehiculos.append(vehiculo)

    def precio_alquiler(self):
        precio=(self.vehiculo.precio_d)*self.dias_alquiler
        return f'El precio es {precio}€'