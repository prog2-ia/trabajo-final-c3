from persona import Persona

class Cliente(Persona):
    def __init__(self,dni,nombre,apellidos,edad,carnet):
        if edad>=18:
            super().__init__(dni,nombre,apellidos)
            self.vehiculos=[]
            self.edad=edad
            self.carnet=carnet
        else:
            print('Edad insuficiente para poder alquilar un vehiculo')