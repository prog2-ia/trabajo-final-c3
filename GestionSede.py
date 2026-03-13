class GestorSede:
    def __init__(self):
        self.sedes = []

    def anadir_sede(self, sede):
        if isinstance(sede,Sede):
            if self.buscar_sede_por_id(sede.idSede) is not None:
                self.sedes.append(sede)

    def buscar_sede_por_id(self, id_sede):
        for sede in self.sedes:
            if sede.id_sede == id_sede:
                return sede
        return None

    def buscar_sede_por_nombre(self, nombre):
        for sede in self.sedes:
            if sede.nombre.lower() == nombre.lower():
                return sede
        return None

