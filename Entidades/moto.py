from Entidades.vehiculo import Vehiculo
#Hereda de vehiculo
class Moto(Vehiculo):
    numero_motos=0   #Contador para saber cuántas motos hay
    def __init__(self,matricula:str,marca:str,modelo:str,color:str,deposito:float,tipo:str,consumo:float,precio_d:float,cilindrada:int)-> None:
        super().__init__(matricula,marca,modelo,color,deposito,tipo,consumo,precio_d)
        self._cilindrada: int=cilindrada
        Moto.numero_motos+=1

    @property
    def cilindrada(self) -> int:          #Creamos cilindrada con @property para mostrar el atributo protegido
        return self._cilindrada