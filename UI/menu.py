from Servicios.GestionCliente import GestionCliente
from Servicios.GestionTrabajador import GestionTrabajador
from Servicios.GestionSede import GestionSede
from Servicios.GestionMantenimiento import GestionMantenimiento
from Servicios.GestionAlquiler import GestionAlquiler


class Menu:
    def __init__(self, gestion_cliente, gestion_trabajador, gestion_sede, gestion_mantenimiento, gestion_alquiler):
        self.gestion_cliente = gestion_cliente
        self.gestion_trabajador = gestion_trabajador
        self.gestion_sede = gestion_sede
        self.gestion_mantenimiento = gestion_mantenimiento
        self.gestion_alquiler = gestion_alquiler

    def elegir_metodo_pago(self):
        metodos = {
            "1": "Tarjeta Credito",
            "2": "Cuenta Bancaria",
            "3": "Cheque",
            "4": "Efectivo"
        }
        print("\nMétodos de pago:")
        for k, v in metodos.items():
            print(f"{k}. {v}")
        op = input("Elige método: ")

        if op in metodos:
            return metodos[op]
        return None

    def menu_clientes(self):
        while True:
            print("\n--- GESTIÓN CLIENTES ---")
            print("1. Añadir cliente")
            print("2. Eliminar cliente")
            print("3. Buscar cliente")
            print("4. Añadir método de pago")
            print("5. Eliminar método de pago")
            print("6. Volver")

            op = int(input("Opción: "))

            if op == 1:
                dni = input("DNI: ")
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                telefono = int(input("Teléfono: "))
                edad = int(input("Edad: "))
                carnet = input("Carnet: ")

                if self.gestion_cliente.añadir_cliente(dni, nombre, apellidos, telefono, edad, carnet):
                    print("Cliente añadido")
                else:
                    print("No se pudo añadir")

            elif op == 2:
                dni = input("DNI: ")
                if self.gestion_cliente.elminar_cliente(dni):
                    print("Cliente eliminado")
                else:
                    print("No existe")

            elif op == 3:
                dni = input("DNI: ")
                cliente = self.gestion_cliente.buscar_cliente(dni)

                if cliente is not None:
                    print(cliente)
                else:
                    print("Cliente no encontrado")

            elif op == 4:
                dni = input("DNI: ")
                metodo = self.elegir_metodo_pago()

                if metodo and self.gestion_cliente.añadir_metodo_pago(dni, metodo):
                    print("Método añadido")
                else:
                    print("Error")

            elif op == 5:
                dni = input("DNI: ")
                metodo = self.elegir_metodo_pago()

                if metodo and self.gestion_cliente.eliminar_metodo_pago(dni, metodo):
                    print("Método eliminado")
                else:
                    print("Error")

            elif op == 6:
                break

    def menu_trabajadores(self):
        while True:
            print("\n--- GESTIÓN TRABAJADORES ---")
            print("1. Contratar trabajador")
            print("2. Despedir trabajador")
            print("3. Buscar trabajador")
            print("4. Mejor vendedor")
            print("5. Volver")

            op = int(input("Opción: "))

            if op == 1:
                cargo = input("Cargo (jefe, vendedor, limpiador): ")
                dni = input("DNI: ")
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                telefono = input("Teléfono: ")
                horas = int(input("Horas: "))

                if self.gestion_trabajador.contratar(cargo, dni, nombre, apellidos, telefono, horas):
                    print("Trabajador contratado")
                else:
                    print("No se pudo contratar")

            elif op == 2:
                dni = input("DNI: ")
                if self.gestion_trabajador.despedir(dni):
                    print("Trabajador despedido")
                else:
                    print("No existe")

            elif op == 3:
                dni = input("DNI: ")
                trabajador = self.gestion_trabajador.buscar_trabajador(dni)

                if trabajador:
                    print(trabajador.dni, trabajador.nombre, trabajador.apellidos, trabajador.telefono)
                else:
                    print("No encontrado")

            elif op == 4:
                vendedor = self.gestion_trabajador.mejor_vendedor()
                if vendedor:
                    print("Mejor vendedor:", vendedor.nombre, vendedor.apellidos, vendedor.dni)
                else:
                    print("No hay vendedores")

            elif op == 5:
                break

    def menu_sedes(self):
        while True:
            print("\n--- GESTIÓN SEDES Y VEHÍCULOS ---")
            print("1. Añadir sede")
            print("2. Añadir coche")
            print("3. Añadir furgoneta")
            print("4. Añadir moto")
            print("5. Eliminar vehículo")
            print("6. Añadir trabajador a sede")
            print("7. Eliminar trabajador de sede")
            print("8. Ver vehículos disponibles")
            print("9. Ver vehículos ocupados")
            print("10. Volver")

            op = int(input("Opción: "))

            if op == 1:
                id_sede = input("ID sede: ")
                nombre = input("Nombre: ")
                ciudad = input("Ciudad: ")
                direccion = input("Dirección: ")
                telefono = input("Teléfono: ")

                if self.gestion_sede.añadir_sede(id_sede, nombre, ciudad, direccion, telefono):
                    print("Sede añadida")
                else:
                    print("No se pudo añadir")

            elif op == 2:
                id_sede = input("ID sede: ")
                matricula = input("Matrícula: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                color = input("Color: ")
                deposito = int(input("Depósito: "))
                tipo = input("Tipo: ")
                consumo = int(input("Consumo: "))
                precio_d = int(input("Precio día: "))
                num_asientos = int(input("Número asientos: "))

                if self.gestion_sede.añadir_coche(id_sede, matricula, marca, modelo, color, deposito, tipo, consumo, precio_d, num_asientos):
                    print("Coche añadido")
                else:
                    print("No se pudo añadir")

            elif op == 3:
                id_sede = input("ID sede: ")
                matricula = input("Matrícula: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                color = input("Color: ")
                deposito = int(input("Depósito: "))
                tipo = input("Tipo: ")
                consumo = int(input("Consumo: "))
                precio_d = int(input("Precio día: "))
                capacidad_carga = int(input("Capacidad de carga: "))
                tamaño = input("Tamaño: ")

                if self.gestion_sede.añadir_furgoneta(id_sede, matricula, marca, modelo, color, deposito, tipo, consumo, precio_d, capacidad_carga, tamaño):
                    print("Furgoneta añadida")
                else:
                    print("No se pudo añadir")

            elif op == 4:
                id_sede = input("ID sede: ")
                matricula = input("Matrícula: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                color = input("Color: ")
                deposito = int(input("Depósito: "))
                tipo = input("Tipo: ")
                consumo = int(input("Consumo: "))
                precio_d = int(input("Precio día: "))
                cilindrada = int(input("Cilindrada: "))

                if self.gestion_sede.añadir_moto(id_sede, matricula, marca, modelo, color, deposito, tipo, consumo, precio_d, cilindrada):
                    print("Moto añadida")
                else:
                    print("No se pudo añadir")

            elif op == 5:
                id_sede = input("ID sede: ")
                matricula = input("Matrícula: ")

                if self.gestion_sede.eleminar_vehiculo(id_sede, matricula):
                    print("Vehículo eliminado")
                else:
                    print("No se pudo eliminar")

            elif op == 6:
                id_sede = input("ID sede: ")
                dni = input("DNI trabajador: ")

                if self.gestion_sede.anadir_trabajador(id_sede, dni):
                    print("Trabajador añadido a la sede")
                else:
                    print("No se pudo añadir")

            elif op == 7:
                id_sede = input("ID sede: ")
                dni = input("DNI trabajador: ")

                if self.gestion_sede.eliminar_trabajador(id_sede, dni):
                    print("Trabajador eliminado de la sede")
                else:
                    print("No se pudo eliminar")

            elif op == 8:
                id_sede = input("ID sede: ")
                lista = self.gestion_sede.lista_vehiculos_disponibles(id_sede)

                if lista is None:
                    print("Sede no encontrada")
                else:
                    for v in lista:
                        print(v.matricula, v.marca, v.modelo)

            elif op == 9:
                id_sede = input("ID sede: ")
                lista = self.gestion_sede.lista_vehiculos_ocupados(id_sede)

                if lista is None:
                    print("Sede no encontrada")
                else:
                    for v in lista:
                        print(v.matricula, v.marca, v.modelo)

            elif op == 10:
                break

    def menu_mantenimiento(self):
        while True:
            print("\n--- GESTIÓN MANTENIMIENTO ---")
            print("1. Añadir avería")
            print("2. Reparar vehículo")
            print("3. Calcular coste reparación")
            print("4. Volver")

            op = int(input("Opción: "))

            if op == 1:
                matricula = input("Matrícula: ")
                print("Averías posibles:")
                print("1. Fallo de motor")
                print("2. Problema de frenos")
                print("3. Batería descargada")
                print("4. Cambio de aceite")
                print("5. Neumático pinchado")
                print("6. Problema en la transmisión")
                print("7. Fallo eléctrico")
                print("8. Radiador dañado")
                print("9. Filtro de aire sucio")
                print("10. Correa de distribución rota")

                averias = {
                    "1": "Fallo de motor",
                    "2": "Problema de frenos",
                    "3": "Batería descargada",
                    "4": "Cambio de aceite",
                    "5": "Neumático pinchado",
                    "6": "Problema en la transmisión",
                    "7": "Fallo eléctrico",
                    "8": "Radiador dañado",
                    "9": "Filtro de aire sucio",
                    "10": "Correa de distribución rota"
                }

                a = input("Avería: ")

                if a not in averias:
                    print("Opción no válida")
                elif self.gestion_mantenimiento.añadir_avería(averias[a], matricula):
                    print("Avería añadida")
                else:
                    print("No se pudo añadir")

            elif op == 2:
                matricula = input("Matrícula: ")
                coste = self.gestion_mantenimiento.reparar_vehiculo(matricula)

                if coste is False:
                    print("No se pudo reparar")
                else:
                    print("Vehículo reparado. Coste:", coste)

            elif op == 3:
                matricula = input("Matrícula: ")
                coste = self.gestion_mantenimiento.calcular_coste(matricula)

                if coste is False:
                    print("Vehículo no encontrado")
                else:
                    print("Coste:", coste)

            elif op == 4:
                break

    def menu_alquileres(self):
        while True:
            print("\n--- GESTIÓN ALQUILERES ---")
            print("1. Crear reserva")
            print("2. Crear alquiler")
            print("3. Buscar alquiler por código")
            print("4. Volver")

            op = int(input("Opción: "))

            if op == 1:
                matricula = input("Matrícula: ")
                fecha_inicio = input("Fecha inicio: ")
                fecha_fin = input("Fecha fin: ")

                if self.gestion_alquiler.crear_reserva(matricula, fecha_inicio, fecha_fin):
                    print("Reserva creada")
                else:
                    print("No se pudo crear")

            elif op == 2:
                dni_c = input("DNI cliente: ")
                matricula = input("Matrícula: ")
                fecha_inicio = input("Fecha inicio: ")
                fecha_fin = input("Fecha fin: ")
                dni_t = input("DNI vendedor: ")

                if self.gestion_alquiler.crear_alquiler(dni_c, matricula, fecha_inicio, fecha_fin, dni_t):
                    print("Alquiler creado")
                else:
                    print("No se pudo crear")

            elif op == 3:
                codigo = input("Código alquiler: ")
                alquiler = self.gestion_alquiler.buscar_alquiler_codigo(codigo)

                if alquiler:
                    print(alquiler.codigo, alquiler.cliente.dni, alquiler.vehiculo.matricula)
                else:
                    print("No encontrado")

            elif op == 4:
                break

    def menu_general(self):
        while True:
            print("\n========== MENÚ GENERAL ==========")
            print("1. Gestión de clientes")
            print("2. Gestión de trabajadores")
            print("3. Gestión de sedes y vehículos")
            print("4. Gestión de mantenimiento")
            print("5. Gestión de alquileres")
            print("6. Salir")

            opcion = int(input("Opción: "))

            if opcion == 1:
                self.menu_clientes()
            elif opcion == 2:
                self.menu_trabajadores()
            elif opcion == 3:
                self.menu_sedes()
            elif opcion == 4:
                self.menu_mantenimiento()
            elif opcion == 5:
                self.menu_alquileres()
            elif opcion == 6:
                print("Saliendo...")
                break

