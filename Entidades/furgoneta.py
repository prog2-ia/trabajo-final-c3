from Entidades.vehiculo import Vehiculo

#
class Furgoneta(Vehiculo):
    def __init__(self,matricula:str,marca:str,modelo:str,color:str,deposito:float,tipo:str,consumo:float,precio_d:float,capacidad_carga:int,tamaño:str)->None:

        super().__init__(matricula,marca,modelo,color,deposito,tipo,consumo,precio_d)
        self.capacidad_carga: int =capacidad_carga
        self.tamaño:str =tamaño

#Función que actualiza el precio según la carga que puede llevar la furgoneta y el tamaño
    def actualizar_tarifa(self) -> bool:
        carga: dict[int, float]={800:1,1000:1.1,1200:1.2}
        self.precio_d*=carga[self.capacidad_carga]

        tamaños: dict[str, int] ={'Pequeña':0,'Mediana':10,'Grande':20}

        if self.tamaño in tamaños:                  #Comprueba que el tamaño exista
            self.precio_d+=tamaños[self.tamaño]
            return True
        else:
            print('Dimension no valida')
            return False