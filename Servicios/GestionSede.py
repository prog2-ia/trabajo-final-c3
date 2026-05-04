from typing import Optional
from Entidades.sede import Sede
from Entidades.coche import Coche
from Entidades.furgoneta import Furgoneta
from Entidades.moto import Moto
from Entidades.vehiculo import Vehiculo
from Entidades.trabajador import Trabajador
from Servicios.GestionTrabajador import GestionTrabajador


class GestionSede:
    def __init__(self, gestor_trabajador: GestionTrabajador) -> None:
        self.sedes: list[Sede] = []
        self.gestor_trabajador: GestionTrabajador = gestor_trabajador

#Función para añadir una sede comprobando que esta no existiese anteriormente
    def añadir_sede(self, id_sede: str, nombre: str, ciudad: str, direccion: str, telefono: str) -> bool:
        if self.buscar_sede_por_id(id_sede) is None:
            sede = Sede(id_sede, nombre, ciudad, direccion, telefono)
            self.sedes.append(sede)
            return True
        return False

    def buscar_sede_por_id(self, id_sede:str)-> Optional[Sede]:
        for sede in self.sedes:
            if sede.idSede == id_sede:
                return sede
        return None

    def buscar_vehiculo(self, matricula:str)-> Optional[Vehiculo]:
        for sede in self.sedes:
            for vehiculo in sede.vehiculos:
                if vehiculo.matricula == matricula:
                    return vehiculo
        return None

#Función que añade un vehiculo comprobando que la sede dada exista y que el vehiculo dado sea nuevo
    def _añadir_vehiculo(self, id_sede: str, clase_vehiculo: type, *args: object) -> bool:
        sede = self.buscar_sede_por_id(id_sede)

        if sede is None:
            return False

        matricula:str=str( args[0])
        if self.buscar_vehiculo(matricula) is not None:
            return False

        vehiculo = clase_vehiculo(*args)
        sede.vehiculos.append(vehiculo)
        return True

    def añadir_coche(self, id_sede: str, matricula: str, marca: str, modelo: str, color: str,
                     deposito: float, tipo: str, consumo: float, precio_d: float, num_asientos: int) -> bool:
        return self._añadir_vehiculo(
            id_sede,
            Coche,
            matricula, marca, modelo, color,
            deposito, tipo, consumo, precio_d, num_asientos
        )

    def añadir_furgoneta(self, id_sede: str, matricula: str, marca: str, modelo: str, color: str,
                         deposito: float, tipo: str, consumo: float, precio_d: float,
                         capacidad_carga: int, tamaño: str) -> bool:
        return self._añadir_vehiculo(
            id_sede,Furgoneta,
            matricula, marca, modelo, color,
            deposito, tipo, consumo, precio_d,
            capacidad_carga, tamaño
        )

    def añadir_moto(self, id_sede: str, matricula: str, marca: str, modelo: str, color: str,
                    deposito: float, tipo: str, consumo: float, precio_d: float, cilindrada: int) -> bool:
        return self._añadir_vehiculo(
            id_sede,
            Moto,
            matricula, marca, modelo, color,
            deposito, tipo, consumo, precio_d, cilindrada
        )

    def eleminar_vehiculo(self, id_sede: str, matricula: str) -> bool:
        vehiculo = self.buscar_vehiculo(matricula)
        sede = self.buscar_sede_por_id(id_sede)

        if vehiculo is None or sede is None:
            return False

        if vehiculo in sede.vehiculos:
            sede.vehiculos.remove(vehiculo)
            return True

        return False



    def mover_vehiculo(self, id_sede1: str, id_sede2: str, matricula: str) -> bool:
        vehiculo = self.buscar_vehiculo(matricula)
        sede1 = self.buscar_sede_por_id(id_sede1)
        sede2 = self.buscar_sede_por_id(id_sede2)
        if vehiculo is None or sede1 is None or sede2 is None:
            return False
        if vehiculo in sede1.vehiculos:
            sede1.vehiculos.remove(vehiculo)
            sede2.vehiculos.append(vehiculo)
            return True
        return False

    def anadir_trabajador(self, id_sede: str, dni: str) -> bool:
        sede = self.buscar_sede_por_id(id_sede)
        if sede is None:
            return False

        trabajador = self.gestor_trabajador.buscar_trabajador(dni)
        if trabajador is None:
            return False

        if trabajador in sede.trabajadores:
            return False

        sede.trabajadores.append(trabajador)
        return True

    def eliminar_trabajador(self, id_sede:str, dni:str)->bool:
        sede = self.buscar_sede_por_id(id_sede)
        if sede is None:
            return False

        trabajador = self.gestor_trabajador.buscar_trabajador(dni)
        if trabajador is None:
            return False

        if trabajador in sede.trabajadores:
            sede.trabajadores.remove(trabajador)
            return True

        return False

    def buscar_trabajador_por_dni(self, dni:str)->Optional[Trabajador]:
        return self.gestor_trabajador.buscar_trabajador(dni)

    def lista_vehiculos_disponibles(self, id_sede: str) -> Optional[list[Vehiculo]]:
        disponibles: list[Vehiculo] = []
        sede = self.buscar_sede_por_id(id_sede)

        if sede is None:
            return None

        for vehiculo in sede.vehiculos:
            if vehiculo.ocupado is False:
                disponibles.append(vehiculo)

        return disponibles

    def lista_vehiculos_ocupados(self, id_sede: str) -> Optional[list[Vehiculo]]:
        ocupados: list[Vehiculo] = []
        sede = self.buscar_sede_por_id(id_sede)

        if sede is None:
            return None

        for vehiculo in sede.vehiculos:
            if vehiculo.ocupado:
                ocupados.append(vehiculo)

        return ocupados