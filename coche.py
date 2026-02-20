class Coche:
    def __init__(self,matricula,marca,modelo,color):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.km_recorridos=0
        self.gasolina=0

    def suma_km(self,km):
        self