from typing import Optional
from datetime import date

from Entidades.alquiler import Alquiler
from Entidades.reserva import Reserva
from Entidades.vehiculo import Vehiculo
from Entidades.vendedor import Vendedor
from Servicios.utils_fecha import string_a_fecha
from Servicios.GestionCliente import GestionCliente
from Servicios.GestionSede import GestionSede
from Servicios.GestionTrabajador import GestionTrabajador


class GestionAlquiler:
    def __init__(self, gestor_cliente: GestionCliente, gestor_sede: GestionSede, gestor_trabajador: GestionTrabajador) -> None:
        self.alquileres: list[Alquiler] = []
        self.gestor_cliente: GestionCliente = gestor_cliente
        self.gestor_sede: GestionSede = gestor_sede
        self.gestor_trabajador: GestionTrabajador = gestor_trabajador

#Función que crea alquiler comprobando que existe el cliente, el vehiculo y el coche dados por los dni y la matrícula
    def crear_alquiler(self, dni_c: str, matricula: str, fecha_i: str, fecha_f: str, dni_t: str) -> bool:
        fecha_inicio:Optional[date] = string_a_fecha(fecha_i)
        fecha_fin:Optional[date] = string_a_fecha(fecha_f)

        cliente = self.gestor_cliente.buscar_cliente(dni_c)
        vehiculo = self.gestor_sede.buscar_vehiculo(matricula)
        trabajador = self.gestor_trabajador.buscar_trabajador(dni_t)

        if cliente is None or vehiculo is None or trabajador is None:
            return False
        if not isinstance(trabajador,Vendedor):  #Se comprueba que el trabajador sea un vendedor
            return False

        if fecha_inicio is None or fecha_fin is None:
            return False

        if fecha_fin < fecha_inicio:
            return False

        if vehiculo.ocupado or not cliente.puede_alquilar():
            return False

        reserva = self.buscar_reserva_exacta(vehiculo, fecha_inicio, fecha_fin)
        if reserva is None:
            return False

        alquiler = Alquiler(cliente, vehiculo, fecha_inicio, fecha_fin, trabajador)
        trabajador.alquileres.append(alquiler)

        self.alquileres.append(alquiler)
        vehiculo.ocupado = True


        return True

#Función que devuelve un alquiler dado por su código si este existe
    def buscar_alquiler_codigo(self, codigo_alquiler: str) -> Optional[Alquiler]:
        for alquiler in self.alquileres:
            if alquiler.codigo == codigo_alquiler:
                return alquiler
        return None

#Función para reservar el coche comprobando que este exista
    def crear_reserva(self, matricula: str, fecha_i: str, fecha_f: str) -> bool:
        vehiculo = self.gestor_sede.buscar_vehiculo(matricula)

        fecha_inicio:Optional[date] = string_a_fecha(fecha_i)
        fecha_fin:Optional[date] = string_a_fecha(fecha_f)

        if vehiculo is None:
            return False

        if fecha_inicio is None or fecha_fin is None:
            return False

        if fecha_fin < fecha_inicio:
            return False

        if self.buscar_reserva_solapada(vehiculo, fecha_inicio, fecha_fin) is None:
            reserva = Reserva(fecha_inicio, fecha_fin)
            vehiculo.reservas.append(reserva)
            return True

        return False


    def buscar_reserva_solapada(self,vehiculo: Vehiculo, fecha_inicio: date, fecha_fin: date) -> Optional[Reserva]:
        for reserva in vehiculo.reservas:
            if reserva.coinciden_fechas(fecha_inicio, fecha_fin):
                return reserva
        return None

#Función que devuelve la reserva dada por las fechas exactas si esta existe
    def buscar_reserva_exacta(self, vehiculo: Vehiculo, fecha_inicio: date, fecha_fin: date) -> Optional[Reserva]:
        for reserva in vehiculo.reservas:
            if reserva.fecha_inicio == fecha_inicio and reserva.fecha_fin == fecha_fin:
                return reserva
        return None

    def eliminar_reserva(self,vehiculo: Vehiculo, fecha_i: str, fecha_f: str) -> bool:
        fecha_inicio:Optional[date] = string_a_fecha(fecha_i)
        fecha_fin:Optional[date] = string_a_fecha(fecha_f)

        if fecha_inicio is None or fecha_fin is None:
            return False

        reserva = self.buscar_reserva_exacta(vehiculo, fecha_inicio, fecha_fin)

        if reserva is None:
            return False

        vehiculo.reservas.remove(reserva)   #Se elimina la reserva de la lista dentro de vehículos
        return True