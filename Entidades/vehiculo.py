# Obj sede
class Vehiculo:
    def __init__(self, matricula:str, marca:str, modelo:str, color:str, deposito:int, tipo:str, consumo:float, precio_d:float):

        self._matricula = matricula
        self._marca = marca
        self._modelo = modelo
        self.precio_d = precio_d
        self.color = color
        self.km_recorridos = 0
        self.gasolina = 0
        self.deposito = deposito
        self.tipo = tipo
        self.averias = []
        self.reservas = []
        self.consumo = consumo
        self.ocupado = False

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
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula}) - KM: {self.km_recorridos} - Combustible: {self.gasolina}/{self.deposito}L"

    def __repr__(self):
        return f"Vehiculo(matricula='{self.matricula}', marca='{self.marca}', modelo='{self.modelo}')"

    def suma_km(self, km:int) -> int:
        self.km_recorridos += km

    def echar_gasolina(self, gasolina:int):
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