from Servicios.GestionCliente import GestionCliente
from Servicios.GestionTrabajador import GestionTrabajador
from Servicios.GestionSede import GestionSede
from Servicios.GestionMantenimiento import GestionMantenimiento
from Servicios.GestionAlquiler import GestionAlquiler
from UI.menu import Menu

if __name__ == "__main__":
    gestor_cliente = GestionCliente()
    gestor_trabajador = GestionTrabajador()
    gestor_sede = GestionSede()
    gestor_sede.gestor_trabajador = gestor_trabajador
    gestor_mantenimiento = GestionMantenimiento(gestor_sede)
    gestor_alquiler = GestionAlquiler(gestor_cliente, gestor_sede, gestor_trabajador)

    # Pseudobase de datos
    gestor_sede.añadir_sede('S1', "Sede Elche", "Elche", "Calle Mayor", "123456789")
    gestor_sede.añadir_sede('S2', "Sede Madrid", "Madrid", "Avenida Perez Lopez nº2", "674323489")

    gestor_sede.añadir_coche('S1', "1234ABC", "Toyota", "Corolla", "Rojo", 50, "gasolina", 6.5, 40, 5)
    gestor_sede.añadir_coche('S1', "2345BCD", "Seat", "Leon", "Blanco", 50, "diesel", 5.0, 45, 5)
    gestor_sede.añadir_coche('S1', "3456CDE", "Tesla", "Model 3", "Negro", 0, "electrico", 0, 70, 5)
    gestor_sede.añadir_coche('S2', "4567DEF", "BMW", "Serie 3", "Azul", 60, "diesel", 6.0, 80, 5)
    gestor_sede.añadir_coche('S2', "5678EFG", "Audi", "A4", "Gris", 55, "gasolina", 6.8, 75, 5)
    gestor_sede.añadir_coche('S2', "6789FGH", "Ford", "Focus", "Verde", 52, "gasolina", 6.2, 38, 5)

    gestor_sede.añadir_furgoneta('S1', "1111AAA", "Mercedes", "Vito", "Blanco", 70, "diesel", 7.5, 90, 1200, "mediana")
    gestor_sede.añadir_furgoneta('S2', "2222BBB", "Renault", "Kangoo", "Gris", 60, "diesel", 6.5, 65, 800, "pequeña")
    gestor_sede.añadir_furgoneta('S2', "3333CCC", "Ford", "Transit", "Azul", 80, "diesel", 8.5, 100, 1500, "grande")

    gestor_sede.añadir_moto('S1', "9999ZZZ", "Yamaha", "MT-07", "Negro", 14, "gasolina", 4.3, 25, 689)
    gestor_sede.añadir_moto('S2', "8888YYY", "Honda", "CB500F", "Rojo", 17, "gasolina", 3.8, 22, 471)

    gestor_cliente.añadir_cliente("12456738Z", "Carlos", "Gomez Perez", 600123456, 30, "B")
    gestor_cliente.añadir_cliente("87654321X", "Maria", "Lopez Ruiz", 611222333, 25, "B")
    gestor_cliente.añadir_cliente("11223344B", "Juan", "Martinez Diaz", 622333444, 40, "C")
    gestor_cliente.añadir_cliente("55667788A", "Lucia", "Fernandez Torres", 633444555, 28, "B")
    gestor_cliente.añadir_cliente("99887766M", "Pedro", "Sanchez Gil", 644555666, 35, "C")

    gestor_trabajador.contratar("jefe", "12345678Z", "Antonio", "Perez Lopez", 600111111, 40)
    gestor_trabajador.contratar("jefe", "87654321H", "Laura", "Gomez Ruiz", 600222222, 40)

    gestor_trabajador.contratar("limpiador", "11223344P", "Carlos", "Martinez Diaz", 600333333, 30)
    gestor_trabajador.contratar("limpiador", "55667788R", "Marta", "Fernandez Torres", 600444444, 30)

    gestor_trabajador.contratar("vendedor", "99887766G", "Juan", "Sanchez Gil", 600555555, 40)
    gestor_trabajador.contratar("vendedor", "44556677D", "Lucia", "Ramirez Soto", 600666666, 40)
    gestor_trabajador.contratar("vendedor", "22334455V", "Pedro", "Navarro Cruz", 600777777, 40)

    gestor_sede.anadir_trabajador('S1', "12345678Z")
    gestor_sede.anadir_trabajador('S2', "87654321H")
    gestor_sede.anadir_trabajador('S1', "11223344P")
    gestor_sede.anadir_trabajador('S2', "55667788R")
    gestor_sede.anadir_trabajador('S1', "99887766G")
    gestor_sede.anadir_trabajador('S1', "44556677D")
    gestor_sede.anadir_trabajador('S2', "22334455V")

    gestor_alquiler.crear_reserva("1234ABC", "01-04-2026", "05-04-2026")
    gestor_alquiler.crear_reserva("5678EFG", "10-04-2026", "15-04-2026")

    menu = Menu(gestor_cliente, gestor_trabajador, gestor_sede, gestor_mantenimiento, gestor_alquiler)
    menu.menu_general()