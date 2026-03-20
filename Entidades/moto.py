from Entidades.vehiculo import Vehiculo
#Hereda de vehiculo
class Moto(Vehiculo):
    numero_motos=0
    def __init__(self,matricula,marca,modelo,color,deposito,tipo,consumo,precio_d,cilindrada):
        super().__init__(matricula,marca,modelo,color,deposito,tipo,consumo,precio_d)
        self._cilindrada=cilindrada
        Moto.numero_motos+=1

    @property
    def cilindrada(self):
        return self._cilindrada
