import vehiculo.py

class GestorMantenimiento:
    def __init__(self):
        pass

    def registrar_averia(self,Tipo,Gravedad,vehiculo):
        averia = {}
        averia['Tipo'] = Tipo
        averia['Gravedad'] = Gravedad
        vehiculo.averías.append(averia)

    def mostrar_averias(self,vehiculo):
        if vehiculo.averías != []:
            for i in range(len(vehiculo.averías)):
                print(f'{i}- Tipo: {vehiculo.averías[i]['Tipo']}, Gravedad: {vehiculo.averías[i]['Tipo']}')
        else:
            print('El vehiculo no tiene ninguna averia')

    def reparar(self,vehiculo):
        lista_repacaiones = {
            "Cambio de Aceite": 80,
            "Pastillas de Freno": 150,
            "Correa de Distribución": 600,
            "Embrague": 850,
            "Pinchazo": 20,
            "Explosión de Motor": 4500,
            "Fallo de Batería (EV)": 3000
        }

        coste_reparacion = 0

        for averia in vehiculo.averías:
            if averia['Tipo'] in lista_repacaiones.keys():
                precio = lista_repacaiones[averia['Tipo']]
                print(f'{averia['Tipo']} tiene un conste de {precio}€')
                coste_reparacion += precio
            else:
                print(f'-{averia['Tipo']}:No se reconoce esta averia')
        print(f'El coste total es: {coste_reparacion}€')
        return coste_reparacion