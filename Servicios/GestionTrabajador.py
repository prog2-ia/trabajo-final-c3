from typing import Optional, Union
from Entidades.vendedor import Vendedor
from Entidades.limpiador import Limpiador
from Entidades.jefe import Jefe
from Entidades.trabajador import Trabajador

class GestionTrabajador:
    def __init__(self)->None:
        self.trabajadores: list[Trabajador] = []

#Función que crea y añade a la lista un trabajador con su cargo específico, comprobando que este sea uno de los existentes
    def contratar(self, cargo: str, dni: str, nombre: str, apellidos: str, telefono: int, horas: int) -> bool:
        if cargo=='limpiador':
            if self.buscar_trabajador(dni) is None:
                limpiador = Limpiador(dni, nombre, apellidos, telefono, horas)
                self.trabajadores.append(limpiador)
                return True
            return False
        elif cargo=='vendedor':
            if self.buscar_trabajador(dni) is None:
                vendedor = Vendedor(dni, nombre, apellidos, telefono, horas)
                self.trabajadores.append(vendedor)
                return True
            return False
        elif cargo=='jefe':
            if self.buscar_trabajador(dni) is None:
                jefe = Jefe(dni, nombre, apellidos, telefono, horas)
                self.trabajadores.append(jefe)
                return True
            return False
        else:
            return False

    def despedir(self,dni:str)->bool:
        trabajador=self.buscar_trabajador(dni)
        if  trabajador is None:
            return False
        self.trabajadores.remove(trabajador)
        return True

    def buscar_trabajador(self,dni:str) -> Optional[Trabajador]:
        for trabajador in self.trabajadores:
            if trabajador.dni==dni:
                return trabajador
        return None

    #Función que devuelve el trabajador que más ventas ha gestionado
    def mejor_vendedor(self)-> Optional[Vendedor]:
        vendedor: Optional[Vendedor]=None
        for i in self.trabajadores:
            if isinstance(i,Vendedor):
                if vendedor is None or i.numero_alquileres()>vendedor.numero_alquileres() :
                    vendedor=i
        return vendedor