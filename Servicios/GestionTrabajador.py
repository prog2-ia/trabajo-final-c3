from Entidades.trabajador import Trabajador
from Entidades.vendedor import Vendedor
from Entidades.limpiador import Limpiador
class GestionTrabajador:
    def __init__(self):
        self.trabajadores=[]

    def contratar(self,cargo,dni,nombre,apellidos,telefono,horas):
        if cargo=='limpiador':
            if self.buscar_trabajador(dni) is None:
                limpiador = Limpiador(dni, nombre, apellidos, telefono, horas)
                self.trabajadores.append(limpiador)
                return True
            return False
        if cargo=='vendedor':
            if self.buscar_trabajador(dni) is None:
                vendedor = Vendedor(dni, nombre, apellidos, telefono, horas)
                self.trabajadores.append(vendedor)
                return True
            return False
        if cargo=='jefe':
            if self.buscar_trabajador(dni) is None:
                jefe = Jefe(dni, nombre, apellidos, telefono, horas)
                self.trabajadores.append(jefe)
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
    def mejor_vendedor(self):
        vendedor=0
        for i in self.trabajadores:
            if isinstance(i,Vendedor):
                if i.numero_alquileres>vendedor.alquileres or vendedor==0:
                    vendedor=i
        return vendedor

