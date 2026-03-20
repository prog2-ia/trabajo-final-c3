# Obj sede
class Vehiculo:
    def __init__(self, matricula, marca, modelo, color, deposito, tipo, consumo, precio_d):

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

    @property
    def matricula(self):
        return self._matricula

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula}) - KM: {self.km_recorridos} - Combustible: {self.gasolina}/{self.deposito}L"

    def __repr__(self):
        return f"Vehiculo(matricula='{self.matricula}', marca='{self.marca}', modelo='{self.modelo}')"

    def suma_km(self, km):
        self.km_recorridos += km

    def echar_gasolina(self, gasolina):
        if self.tipo == 'eléctrico':
            print('Has intentado echar gasolina en un coche eléctrico.')
            self.averias.append('Explosión de motor por combustible')
        else:
            if self.gasolina + gasolina <= self.deposito:
                self.gasolina += gasolina
            else:
                print("No se puede echar gasolina por encima del límite")
                self.gasolina = self.deposito

    def mostrar_averias(self):
        for i in self.averias:
            print(i)