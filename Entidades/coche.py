from Entidades.vehiculo import Vehiculo
#Clase Coche con contador de coches
class Coche(Vehiculo):
    num_coche=0
    def __init__(self,matricula,marca,modelo,color,deposito,tipo,consumo,precio_d,num_asientos):
        super().__init__(matricula,marca,modelo,color,deposito,tipo,consumo,precio_d)
        self.num_asientos=num_asientos
        Coche.num_coche+=1