from Entidades.alquiler import Alquiler



class GestionAlquiler:
    def __init__(self, gestor_cliente, gestor_sede):
        self.alquileres = []
        self.gestor_cliente = gestor_cliente
        self.gestor_sede = gestor_sede

    def crear_alquiler(self,dni_c,matricula,dias_alquiler,dni_t):
        cliente=self.gestor_cliente.buscar_cliente(dni_c)
        vehiculo=self.gestor_sede.buscar_vehiculo(matricula)
        trabajador=self.gestor_sede.buscar_trabajador_por_dni(dni_t)
        if cliente is None or vehiculo is None or trabajador is None:
            return False

        if vehiculo.ocupado or not(cliente.puede_alquiler()):
            return False
        alquiler=Alquiler(cliente,vehiculo,dias_alquiler,trabajador)
        self.alquileres.append((alquiler))
        return True

    def buscar_alquiler_codigo(self,codio_alquiler):
        for alquiler in self.alquileres:
            if alquiler.codigo==codio_alquiler:
                return alquiler
        return None


