from UbuntuDrivers.detect import get_linux_image_from_meta

from vehiculo import Vehiculo


class Sede:
    ids_sedes=[]
    def __init__(self,idSede,nombre,ciudad,direccion,telefono):
        if idSede not in type(self).ids_sedes:
            self.idSede=idSede
            self.nombre=nombre
            self.ciudad=ciudad
            self.direccion=direccion
            self.telefono=telefono
            self.vehiculos=[]
            self.empleados=[]
            type(self).ids_sedes.append(idSede)
        else:
            print(f'La id {idSede} ya existe')

    def añadir_vehiculo(self,vehiculo):
        if isinstance(vehiculo,Vehiculo):
            if vehiculo not in self.vehiculos:
                self.vehiculos.append(vehiculo)
            else:
                print('El vehiculo ya se encuentra en la sede')
                return False

            return True
        else:
            print('Valor erroneo. Introduca un vehiculo')
            return False

    def lista_vehiculos_disponibles(self):
        print('Los vehiculos disponibles son: ')
        for vehiculo in self.vehiculos:
            if vehiculo.ocupado==False:
                print('-',vehiculo.__str__())

    def lista_vehiculos_alquilados(self):
        print('Los vehiculos alquilados son: ')
        for vehiculo in self.vehiculos:
            if vehiculo.ocupado:
                print('-',vehiculo.__str__())

    def eliminar_vehiculo(self,matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula==matricula:
                self.vehiculos.remove(vehiculo)
                return True
        print(f'No se ha encontrado el vehiculo')
        return False

    def mover_vehiculo(self,vehiculo,destino):
        if isinstance(vehiculo,Vehiculo) and isinstance(destino,Sede):
            if self.eliminar_vehiculo(vehiculo.matricula):
                if destino.añadir_vehiculo(vehiculo):
                    return True
                else:
                    return False
            else:
                return False
        else:
            print('Valores erroneos')
            return False

