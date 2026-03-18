from Entidades.trabajador import Trabajador
class GestionTrabajador:
    def __init__(self):
        self.trabajadores=[]

    def contratar(self,dni,nombre,apellidos,telefono,horas):
        if self.buscar_trabajador(dni) is None:
            trabajador=Trabajador(dni,nombre,apellidos,telefono,horas)
            self.trabajadores.append(trabajador)
            return True
        return False

    def despedir(self,dni):
        trabajador=self.buscar_trabajador(dni)
        if  trabajador is None:
            return False
        self.trabajadores.remove(trabajador)
        return True

    def buscar_trabajador(self,dni):
        for trabajador in self.trabajadores:
            if trabajador.dni==dni:
                return trabajador
        return None