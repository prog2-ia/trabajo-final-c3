from Entidades.cliente import Cliente


class GestionCliente:
    def __init__(self):
        self.clientes=[]

    def añadir_cliente(self,dni,nombre,apellidos,telefono,edad,carnet):
        if self.buscar_cliente(dni) is None:
            cliente=Cliente(dni,nombre,apellidos,telefono,edad,carnet)
            self.clientes.append(cliente)
            return True
        return False

    def elminar_cliente(self,dni):
        cliente=self.buscar_cliente(dni)
        if  cliente is None:
            return False
        self.clientes.remove(cliente)
        return True

    def buscar_cliente(self,dni):
        for cliente in self.clientes:
            if cliente.dni==dni:
                return cliente
        return None

    def añadir_metodo_pago(self,dni,metodo):
        cliente=self.buscar_cliente(dni)
        if cliente is None:
            return False

        metodos=['Tarjeta Credito','Cuenta Bancaria','Cheque','Efectivo']

        if metodo in metodos and metodo and metodo not in cliente.metodo_pago:
            cliente.metodo_pago.append(metodo)
            return True
        else:
            return  False

    def eliminar_metodo_pago(self,dni,metodo):
        cliente=self.buscar_cliente(dni)
        if cliente is None:
            return False

        metodos=['Tarjeta Credito','Cuenta Bancaria','Cheque','Efectivo']

        if metodo in metodos and metodo and metodo  in cliente.metodo_pago:
            cliente.metodo_pago.remove(metodo)
            return True
        else:
            return  False

