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


class Cliente:
    def __init__(self,DNI,nombre,apellido):
        self.dni=DNI
        self.nombre=nombre
        self.apellido=apellido
        self.vehiculos=[]


class Alquiler:
    def __init__(self,cliente,vehiculo,dias_alquiler,trabajador):
        self.cliente=cliente
        self.vehiculo=vehiculo
        self.trabajador=trabajador
        self.dias_alquiler=dias_alquiler
        self.cliente.vehiculos.append(vehiculo)

    def precio_alquiler(self):
        precio=(self.vehiculo.precio_d)*self.dias_alquiler
        return f'El precio es {precio}€'





class Trabajador:
    def __init__(self,dni,nombre,apellidos,cargo,sueldo):
        self.dni=dni
        self.apellidos=apellidos
        self.cargo=cargo
        self.sueldo=sueldo
        self.ventas=0

    def aumento(self,dinero):
        self.sueldo+=dinero
        print('El sueldo de ',self,' ha aumentado a ',self.sueldo,'€.')
