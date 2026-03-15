#Obj sede
class Vehiculo:
    def __init__(self,matricula,marca,modelo,color,deposito,tipo,consumo,precio_d):
        self.matricula=matricula
        self.precio_d=precio_d
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.km_recorridos=0
        self.gasolina=0
        self.deposito=deposito
        self.tipo=tipo
        self.averías=[]
        self.consumo=consumo
        self.ocupado=False

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula}) - KM: {self.km_recorridos} - Combustible: {self.gasolina}/{self.deposito}L"

    def __repr__(self):
        return f"Vehiculo(matricula='{self.matricula}', marca='{self.marca}', modelo='{self.modelo}')"

    def suma_km(self,km):
        self.km_recorridos+=km


    def echar_gasolina(self,gasolina):
        if self.tipo=='eléctrico':
            print('Has intentado echar gasolina en un coche eléctrico, tu motor ha sufrido una explosión.')
            self.averías.append('Explosion de motor por combustible')
        else:
            if self.gasolina+gasolina<=self.deposito:
                self.gasolina+=gasolina
            else:
                print("No se puede hechar gasolina por encima del limite")
                self.gasolina=self.deposito
    def mostrar_averias(self):

        for i in self.averías:
            print(i)


