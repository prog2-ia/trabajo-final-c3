import cliente.py
#Obj Cliente
class GestorCliente:
    def __init__(self):
        self.clientes=[]
        pass
    def registrar_cliente(self,cliente):
        if cliente.dni not in self.clientes:
            clientes.append(cliente.dni)


    def añadir_metodo_pago(self,metodo,cliente):
        if metodo not in cliente.metodo_pago:
            cliente.metodo_pago.append(metodo)
        else:
            print('El método ya había sido añadido')

    def sumar_puntos(self,puntos,cliente):
        cliente.puntos+=puntos
