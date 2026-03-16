from Entidades.alquiler import Alquiler
from Servicios.utils_fecha import string_a_fecha
from Entidades.reserva import Reserva


class GestionAlquiler:
    def __init__(self, gestor_cliente, gestor_sede):
        self.alquileres = []
        self.gestor_cliente = gestor_cliente
        self.gestor_sede = gestor_sede

    def crear_alquiler(self, dni_c, matricula, fecha_inicio, fecha_fin, dni_t):
        cliente = self.gestor_cliente.buscar_cliente(dni_c)
        vehiculo = self.gestor_sede.buscar_vehiculo(matricula)
        trabajador = self.gestor_sede.buscar_trabajador_por_dni(dni_t)

        fecha_inicio = string_a_fecha(fecha_inicio)
        fecha_fin = string_a_fecha(fecha_fin)

        if cliente is None or vehiculo is None or trabajador is None:
            return False

        if fecha_fin < fecha_inicio:
            return False

        if vehiculo.ocupado or not cliente.puede_alquilar():
            return False

        alquiler = Alquiler(cliente, vehiculo, fecha_inicio, fecha_fin, trabajador)
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

        if fecha_fin < fecha_inicio:
            return False

        if self.buscar_reserva(vehiculo, fecha_inicio, fecha_fin) is None:
            reserva = Reserva(fecha_inicio, fecha_fin)
            vehiculo.reservas.append(reserva)
            return True

        return False

    def buscar_reserva(self, vehiculo, fecha_inicio, fecha_fin):
        for reserva in vehiculo.reservas:
            if reserva.coinciden_fechas(fecha_inicio, fecha_fin):
                return reserva
        return None

    def eliminar_reserva(self, vehiculo, fecha_inicio, fecha_fin):
        reserva = self.buscar_reserva(vehiculo, fecha_inicio, fecha_fin)

        if reserva is None:
            return False

        vehiculo.reservas.remove(reserva)
        return True