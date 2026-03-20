from Entidades.vehiculo import Vehiculo

#
class Furgoneta(Vehiculo):
    def __init__(self,matricula,marca,modelo,color,deposito,tipo,consumo,precio_d,capacidad_carga,tamaño):

        super().__init__(matricula,marca,modelo,color,deposito,tipo,consumo,precio_d)
        self.capacidad_carga=capacidad_carga
        self.tamaño=tamaño

    def actualizar_tarifa(self):
        carga={800:1,1000:1.1,1200:1.2}
        self.precio_d*=carga[self.capacidad_carga]

        tamaños={'Pequeña':0,'Mediana':10,'Grande':20}

        if self.tamaño in tamaños:
            self.precio_d+=tamaños[self.tamaño]
            return True
        else:
            print('Dimension no valida')
            return False


