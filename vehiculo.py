class Vehiculo:
    numero_vehiculos=0
    def __init__(self,matricula,marca,modelo,color,deposito,tipo,precio_d):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.km_recorridos=0
        self.gasolina=0
        self.deposito=deposito
        self.tipo=tipo
        self.averías=[]
        self.precio_d=precio_d
        type(self).numero_vehiculos+=1

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

    def ocupado(self):
