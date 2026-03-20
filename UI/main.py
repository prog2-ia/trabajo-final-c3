from Entidades.coche import Coche
from Entidades.furgoneta import Furgoneta
from Entidades.moto import Moto
from Servicios.GestionSede import GestionSede
from Servicios.GestionTrabajador import GestionTrabajador
from Servicios.GestionCliente import GestionCliente
from Servicios.GestionAlquiler import GestionAlquiler


if __name__ == "__main__":
    gestor_cliente=GestionCliente()
    gestor_trabajador=GestionTrabajador()

