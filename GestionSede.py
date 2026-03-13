from Entidades.vehiculo import Vehiculo
from Entidades.sede import Sede


class GestorSede:
    def __init__(self):
        self.sedes = []

    def anadir_sede(self, sede):
        if isinstance(sede, Sede):
            if self.buscar_sede_por_id(sede.idSede) is None:
                self.sedes.append(sede)
                return True
        return False

    def buscar_sede_por_id(self, id_sede):
        for sede in self.sedes:
            if sede.idSede == id_sede:
                return sede
        return None

    def buscar_sede_por_nombre(self, nombre):
        for sede in self.sedes:
            if sede.nombre.lower() == nombre.lower():
                return sede
        return None

    def añadir_vehiculo(self, id_sede, vehiculo):
        sede = self.buscar_sede_por_id(id_sede)

        if sede is not None and isinstance(vehiculo, Vehiculo):
            if self.buscar_vehiculo(vehiculo.matricula) is None:
                sede.vehiculos.append(vehiculo)
                return True
        return False

    def eleminar_vehiculo(self,id_sede,matricula):
        vehiculo=self.buscar_vehiculo(matricula)
        sede=self.buscar_sede_por_id(id_sede)
        if vehiculo is  None or sede is None:
            return False

        if vehiculo in sede.vehiculos:
            sede.vehiculos.remove(vehiculo)
            return True

        return False

    def buscar_vehiculo(self, matricula):
        for sede in self.sedes:
            for vehiculo in sede.vehiculos:
                if vehiculo.matricula == matricula:
                    return vehiculo
        return None

    def mover_vehiculo(self,id_sede1,id_sede2,matricula):
        vehiculo=self.buscar_vehiculo(matricula)
        sede1=self.buscar_sede_por_id(id_sede1)
        sede2=self.buscar_sede_por_id(id_sede2)

        if vehiculo is None or sede1 is None or sede2 is None:
            return  False

        if self.eleminar_vehiculo(id_sede1,matricula):
            pass
            if self.añadir_vehiculo(id_sede2,vehiculo):
                return True

        return False




