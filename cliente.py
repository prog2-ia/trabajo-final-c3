from persona import Persona

class Cliente(Persona):
    def __init__(self,dni,nombre,apellidos):
        super().__init__(dni,nombre,apellidos)
        self.vehiculos=[]