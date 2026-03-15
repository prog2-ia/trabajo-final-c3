form Entidades.alquiler import Alquiler

class GestionAlquiler:
    def __init__(self):
        self.alquileres=[]

    def crear_alquiler(self,alquiler):
        if isinstance(alquiler,Alquiler):
            pass
        return False

    def busca_cliente(self,dni):
        for alquiler in self.alquileres:
            cliente=alquiler.cliente
            if cliente.dni==dni:
                return cliente
        return None
