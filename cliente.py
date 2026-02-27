class Cliente:
    def __init__(self,dni,nombre,apellidos):
        super().__init__(dni,nombre,apellidos)
        self.vehiculos=[]