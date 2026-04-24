from Entidades.vehiculo import Vehiculo
#Clase Coche con contador de coches
class Coche(Vehiculo):
    num_coche=0
    def __init__(self,matricula:str,marca:str,modelo:str,color:str,deposito:int,tipo:str,consumo:float,precio_d:float,num_asientos:int)-> None:
        super().__init__(matricula,marca,modelo,color,deposito,tipo,consumo,precio_d)
        self.num_asientos: int =num_asientos
        Coche.num_coche+=1