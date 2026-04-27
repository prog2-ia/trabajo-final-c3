from typing import Optional
from Entidades.cliente import Cliente


class GestionCliente:
    def __init__(self)->None:
        self.clientes:list[Cliente]=[]

#Función que añade un cliente si este no existia antes
    def añadir_cliente(self,dni: str, nombre: str, apellidos: str, telefono: int, edad: int, carnet: str) -> bool:
        if self.buscar_cliente(dni) is None:
            cliente=Cliente(dni,nombre,apellidos,telefono,edad,carnet)
            self.clientes.append(cliente)
            return True
        return False

#Función que elimina un cliente de la lista de clientes
    def elminar_cliente(self,dni:str)->bool:
        cliente=self.buscar_cliente(dni)
        if  cliente is None:
            return False
        self.clientes.remove(cliente)
        return True

    def buscar_cliente(self,dni:str)->Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.dni==dni:
                return cliente
        return None

    def añadir_metodo_pago(self,dni: str, metodo: str) -> bool:
        cliente=self.buscar_cliente(dni)
        if cliente is None:
            return False

        metodos=['Tarjeta Credito','Cuenta Bancaria','Cheque','Efectivo']

#Se comprueba que el metodo es uno de los existentes y que el cliente no lo poseia antes
        if metodo in metodos and metodo and metodo not in cliente.metodo_pago:
            cliente.metodo_pago.append(metodo)
            return True
        else:
            return  False

    def eliminar_metodo_pago(self,dni: str, metodo: str) -> bool:
        cliente=self.buscar_cliente(dni)
        if cliente is None:
            return False

        metodos=['Tarjeta Credito','Cuenta Bancaria','Cheque','Efectivo']

        if metodo in metodos and metodo and metodo  in cliente.metodo_pago:
            cliente.metodo_pago.remove(metodo)
            return True
        else:
            return  False