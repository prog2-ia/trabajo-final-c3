from Entidades.sede import Sede
from Entidades.coche import Coche
from Entidades.furgoneta import Furgoneta
from Entidades.moto import Moto


class GestionSede:
    def __init__(self,gestor_trabajador):
        self.sedes = []
        self.gestor_trabajador=gestor_trabajador

#Función para añadir una sede comprobando que esta no existiese anteriormente
    def añadir_sede(self, id_sede, nombre, ciudad, direccion, telefono):
        if self.buscar_sede_por_id(id_sede) is None:
            sede = Sede(id_sede, nombre, ciudad, direccion, telefono)
            self.sedes.append(sede)
            return True
        return False

    def buscar_sede_por_id(self, id_sede):
        for sede in self.sedes:
            if sede.idSede == id_sede:
                return sede
        return None

    def buscar_vehiculo(self, matricula):
        for sede in self.sedes:
            for vehiculo in sede.vehiculos:
                if vehiculo.matricula == matricula:
                    return vehiculo
        return None

#Función que añade un vehiculo comprobando que la sede dada exista y que el vehiculo dado sea nuevo
    def _añadir_vehiculo(self, id_sede, clase_vehiculo, *args):
        sede = self.buscar_sede_por_id(id_sede)

        if sede is None:
            return False

        matricula = args[0]
        if self.buscar_vehiculo(matricula) is not None:
            return False

        vehiculo = clase_vehiculo(*args)
        sede.vehiculos.append(vehiculo)
        return True

    def añadir_coche(self, id_sede, matricula, marca, modelo, color,
                     deposito, tipo, consumo, precio_d, num_asientos):
        return self._añadir_vehiculo(
            id_sede,
            Coche,
            matricula, marca, modelo, color,
            deposito, tipo, consumo, precio_d, num_asientos
        )

    def añadir_furgoneta(self, id_sede, matricula, marca, modelo, color,
                         deposito, tipo, consumo, precio_d,
                         capacidad_carga, tamaño):
        return self._añadir_vehiculo(
            id_sede,
            Furgoneta,
            matricula, marca, modelo, color,
            deposito, tipo, consumo, precio_d,
            capacidad_carga, tamaño
        )

    def añadir_moto(self, id_sede, matricula, marca, modelo, color,
                    deposito, tipo, consumo, precio_d, cilindrada):
        return self._añadir_vehiculo(
            id_sede,
            Moto,
            matricula, marca, modelo, color,
            deposito, tipo, consumo, precio_d, cilindrada
        )

    def eleminar_vehiculo(self, id_sede, matricula):
        vehiculo = self.buscar_vehiculo(matricula)
        sede = self.buscar_sede_por_id(id_sede)

        if vehiculo is None or sede is None:
            return False

        if vehiculo in sede.vehiculos:
            sede.vehiculos.remove(vehiculo)
            return True

        return False



    def mover_vehiculo(self, id_sede1, id_sede2, matricula):
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

    def anadir_trabajador(self, id_sede, dni):
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

    def eliminar_trabajador(self, id_sede, dni):
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

    def buscar_trabajador_por_dni(self, dni):
        return self.gestor_trabajador.buscar_trabajador(dni)

    def lista_vehiculos_disponibles(self, id_sede):
        disponibles = []
        sede = self.buscar_sede_por_id(id_sede)

        if sede is None:
            return None

        for vehiculo in sede.vehiculos:
            if vehiculo.ocupado is False:
                disponibles.append(vehiculo)

        return disponibles

    def lista_vehiculos_ocupados(self, id_sede):
        ocupados = []
        sede = self.buscar_sede_por_id(id_sede)

        if sede is None:
            return None

        for vehiculo in sede.vehiculos:
            if vehiculo.ocupado:
                ocupados.append(vehiculo)

        return ocupados