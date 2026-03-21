from Entidades.persona import Persona
#Obj: Alquiler
class Cliente(Persona):
    def __init__(self,dni,nombre,apellidos,telefono,edad,carnet):
        if edad>=18 :                                        #Al crear el cliente comprobamos que sea mayor de edad
            super().__init__(dni,nombre,apellidos,telefono)
            self.vehiculos=[]
            self.edad=edad
            self.carnet=carnet
            self.metodo_pago=[]
            self.puntos=0
#Creamos metodo str()
    def __str__(self):
        return f'{type(self).__name__}: {self.dni} {self.nombre} {self.apellidos} {self.telefono}'

#Función que comprueba que el cliente tiene forma de pagar
    def puede_alquilar(self):
        if self.metodo_pago==[]:
            return False
        return True


