from vehiculo import Vehiculo

class Coche(Vehiculo):
    num_coche=0
    def __init__(self,matricula,marca,modelo,color,deposito,tipo,precio_d,num_asientos):
        super().__init__(matricula,marca,modelo,color,deposito,tipo,precio_d)
        self.num_asientos=num_asientos
