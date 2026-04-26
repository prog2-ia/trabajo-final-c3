from Entidades.persona import Persona
from Entidades.vehiculo import Vehiculo
#Obj: Alquiler
class Cliente(Persona):
    def __init__(self, dni: str, nombre: str, apellidos: str, telefono: int, edad: int, carnet: str) -> None:
        if edad>=18 :                                        #Al crear el cliente comprobamos que sea mayor de edad
            super().__init__(dni,nombre,apellidos,telefono)
            self.vehiculos: list[Vehiculo] = []
            self.edad: int = edad
            self.carnet: str = carnet
            self.metodo_pago: list[str] = []
            self.puntos: int = 0
#Creamos metodo str()
    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.dni} {self.nombre} {self.apellidos} {self.telefono}'

#Función que comprueba que el cliente tiene forma de pagar
    def puede_alquilar(self) -> bool :
        if self.metodo_pago==[]:
            return False
        return True