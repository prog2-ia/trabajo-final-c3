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
        self.ocupado=False
        Vehiculo.numero_vehiculos+=1

    def __str__(self):
        if self.ocupado:
             estado= "OCUPADO"
        else:
            estado="LIBRE"
        return f"[{self.matricula}] {self.marca} {self.modelo} ({estado}) - {self.gasolina}/{self.deposito}L"

    def suma_km(self,km):
        self.km_recorridos+=km
    def nueva_averia(self,Tipo,Gravedad):
        averia={}
        averia['Tipo']=Tipo
        averia['Gravedad']=Gravedad
        self.averías.append(averia)


    def echar_gasolina(self,gasolina):
        if self.tipo=='eléctrico':
            print('Has intentado echar gasolina en un coche eléctrico, tu motor ha sufrido una explosión.')
            self.nueva_averia('Explosión de motor','Alta')
        else:
            if self.gasolina+gasolina<=self.deposito:
                self.gasolina+=gasolina
            else:
                print("No se puede hechar gasolina por encima del limite")
                self.gasolina=self.deposito


    def mostrar_averias(self):
        if self.averías != []:
            for i in range(len(self.averías)):
                print(f'{i}- Tipo: {self.averías[i]['Tipo']}, Gravedad: {self.averías[i]['Tipo']}')
        else:
            print('El vehiculo no tiene ninguna averia')

    def reparar(self):
        lista_repacaiones = {
            "Cambio de Aceite": 80,
            "Pastillas de Freno": 150,
            "Correa de Distribución": 600,
            "Embrague": 850,
            "Pinchazo": 20,
            "Explosión de Motor": 4500,
            "Fallo de Batería (EV)": 3000
        }

        coste_reparacion=0

        for averia in self.averías:
            if averia['Tipo'] in lista_repacaiones.keys():
                precio=lista_repacaiones[averia['Tipo']]
                print(f'{averia['Tipo']} tiene un conste de {precio}€')
                coste_reparacion+=precio
            else:
                print(f'-{averia['Tipo']}:No se reconoce esta averia')
        print(f'El coste total es: {coste_reparacion}€')
        return coste_reparacion

