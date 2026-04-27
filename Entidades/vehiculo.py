from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Entidades.reserva import Reserva

# Obj sede
class Vehiculo:
    def __init__(self, matricula:str, marca:str, modelo:str, color:str, deposito:float, tipo:str, consumo:float, precio_d:float)->None:

        self._matricula: str = matricula
        self._marca: str = marca
        self._modelo: str = modelo
        self.precio_d: float = precio_d
        self.color: str = color
        self.km_recorridos: float = 0
        self.gasolina: float = 0
        self.deposito: float = deposito
        self.tipo: str = tipo
        self.averias: list[str] = []
        self.reservas: list[Reserva] = []
        self.consumo: float = consumo
        self.ocupado: bool = False

#Creamos funciones con @property para mostrar los atributos protegidos
    @property
    def matricula(self) -> str:
        return self._matricula

    @property
    def marca(self) -> str:
        return self._marca

    @property
    def modelo(self) -> str:
        return self._modelo

#Creamos metodos str y repr
    def __str__(self)->str:
        return f"{self.marca} {self.modelo} ({self.matricula}) - KM: {self.km_recorridos} - Combustible: {self.gasolina}/{self.deposito}L"

    def __repr__(self)->str:
        return f"Vehiculo(matricula='{self.matricula}', marca='{self.marca}', modelo='{self.modelo}')"

    def suma_km(self, km:int) -> None:
        self.km_recorridos += km

    def echar_gasolina(self, gasolina:float)->None:
        if self.tipo == 'eléctrico':                                     #Si se echa gasolina a un coche eléctrico se avería
            print('Has intentado echar gasolina en un coche eléctrico.')
            self.averias.append('Explosión de motor por combustible')
        else:
            if self.gasolina + gasolina <= self.deposito:
                self.gasolina += gasolina
            else:
                print("No se puede echar gasolina por encima del límite")
                self.gasolina = self.deposito

    def mostrar_averias(self) -> None:
        for i in self.averias:
            print(i)