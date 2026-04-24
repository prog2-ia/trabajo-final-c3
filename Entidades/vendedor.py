from Entidades.trabajador import Trabajador

class Vendedor(Trabajador):
    def __init__(self,dni:str,nombre:str,apellidos:str,telefono:int,horas:int):
        super().__init__(dni, nombre, apellidos, telefono,horas)
        self.alquileres=[]
        self.sueldo=self.calcular_sueldo()

    def calcular_sueldo(self) -> int :
        sueldo=self.horas*15
        return sueldo

#Función para ver cuantos alquileres ha gestionado
    def numero_alquileres(self) -> int:
        numero=len(self.alquileres)
        return numero