class Vehiculo:
    def __init__(self,matricula,marca,modelo,color,deposito,tipo):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.km_recorridos=0
        self.gasolina=0
        self.deposito=deposito
        self.tipo=tipo

    def suma_km(self,km):
        self.km_recorridos+=km


    def hechar_gasolina(self,gasolina):
        if self.gasolina+gasolina<=self.deposito:
            self.gasolina+=gasolina
        else:
            print("No se puede hechar gasolina por encima del limite")
            self.gasolina=self.deposito
