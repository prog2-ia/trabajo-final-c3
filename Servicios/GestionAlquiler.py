from Entidades.alquiler import Alquiler
from Servicios.utils_fecha import string_a_fecha
from Entidades.reserva import Reserva
from Entidades.vendedor import Vendedor


class GestionAlquiler:
    def __init__(self, gestor_cliente, gestor_sede,gestor_trabajador):
        self.alquileres = []
        self.gestor_cliente = gestor_cliente
        self.gestor_sede = gestor_sede
        self.gestor_trabajador=gestor_trabajador

    def crear_alquiler(self, dni_c, matricula, fecha_inicio, fecha_fin, dni_t):
        fecha_inicio = string_a_fecha(fecha_inicio)
        fecha_fin = string_a_fecha(fecha_fin)

        cliente = self.gestor_cliente.buscar_cliente(dni_c)
        vehiculo = self.gestor_sede.buscar_vehiculo(matricula)
        trabajador = self.gestor_trabajador.buscar_trabajador(dni_t)

        if cliente is None or vehiculo is None or trabajador is None:
            return False
        if not isinstance(trabajador,Vendedor):
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

    def buscar_alquiler_codigo(self, codigo_alquiler):
        for alquiler in self.alquileres:
            if alquiler.codigo == codigo_alquiler:
                return alquiler
        return None

    def crear_reserva(self, matricula, fecha_inicio, fecha_fin):
        vehiculo = self.gestor_sede.buscar_vehiculo(matricula)

        fecha_inicio = string_a_fecha(fecha_inicio)
        fecha_fin = string_a_fecha(fecha_fin)

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


    def buscar_reserva_solapada(self, vehiculo, fecha_inicio, fecha_fin):
        for reserva in vehiculo.reservas:
            if reserva.coinciden_fechas(fecha_inicio, fecha_fin):
                return reserva
        return None

    def buscar_reserva_exacta(self, vehiculo, fecha_inicio, fecha_fin):
        for reserva in vehiculo.reservas:
            if reserva.fecha_inicio == fecha_inicio and reserva.fecha_fin == fecha_fin:
                return reserva
        return None

    def eliminar_reserva(self, vehiculo, fecha_inicio, fecha_fin):
        fecha_inicio = string_a_fecha(fecha_inicio)
        fecha_fin = string_a_fecha(fecha_fin)

        if fecha_inicio is None or fecha_fin is None:
            return False

        reserva = self.buscar_reserva_exacta(vehiculo, fecha_inicio, fecha_fin)

        if reserva is None:
            return False

        vehiculo.reservas.remove(reserva)
        return True