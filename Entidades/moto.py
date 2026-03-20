from Entidades.vehiculo import Vehiculo
#Hereda de vehiculo
class Moto(Vehiculo):
    numero_motos=0
    def __init__(self,matricula,marca,modelo,color,deposito,tipo,consumo,precio_d):
        super().__init__(matricula,marca,modelo,color,deposito,tipo,consumo,precio_d)
        Moto.numero_motos+=1