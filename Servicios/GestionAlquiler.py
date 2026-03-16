from Entidades.alquiler import Alquiler
from Servicios.utils_fecha import string_a_fecha,diferecia_dias
class GestionAlquiler:
    def __init__(self, gestor_cliente, gestor_sede):
        self.alquileres = []
        self.gestor_cliente = gestor_cliente
        self.gestor_sede = gestor_sede

    def crear_alquiler(self,dni_c,matricula,fecha_inicio,fecha_fin,dni_t):
        cliente=self.gestor_cliente.buscar_cliente(dni_c)
        vehiculo=self.gestor_sede.buscar_vehiculo(matricula)
        trabajador=self.gestor_sede.buscar_trabajador_por_dni(dni_t)
        fecha_inicio=string_a_fecha(fecha_inicio)
        fecha_fin=string_a_fecha(fecha_fin)

        if cliente is None or vehiculo is None or trabajador is None:
            return False
        if vehiculo.ocupado or not(cliente.puede_alquiler()):
            return False
        if fecha_fin<fecha_inicio:
            return True
        alquiler=Alquiler(cliente,vehiculo,fecha_inicio,fecha_fin,trabajador)
        self.alquileres.append((alquiler))
        return True

    def buscar_alquiler_codigo(self,codio_alquiler):
        for alquiler in self.alquileres:
            if alquiler.codigo==codio_alquiler:
                return alquiler
        return None


