from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Entidades.vehiculo import Vehiculo
    from Entidades.trabajador import Trabajador

class Sede:
    def __init__(self, idSede:str, nombre:str, ciudad:str, direccion:str, telefono:str)->None:
        self.idSede:str = idSede
        self.nombre:str = nombre
        self.ciudad:str = ciudad
        self.direccion:str = direccion
        self.telefono:str = telefono
        self.vehiculos: list[Vehiculo] = []
        self.trabajadores: list[Trabajador] = []