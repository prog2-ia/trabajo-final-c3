from persona import Persona

class Cliente(Persona):
    def __init__(self,dni,nombre,apellidos,edad,carnet):
        if edad>=18:
            super().__init__(dni,nombre,apellidos)
            self.vehiculos=[]
            self.edad=edad
            self.carnet=carnet
            self.metodo_pago=[]
        else:
            print('Edad insuficiente para poder alquilar un vehiculo')

    def añadir_metodo_pago(self,metodo):
        metodos=['Tarjetas','Cuenta Bancaria','Cheque','Efectivo']

        if metodo in metodos:
            self.metodo_pago.append(metodo)
            return True
        else:
            print(f'El metodo {metodo} no es valido')
            return  False