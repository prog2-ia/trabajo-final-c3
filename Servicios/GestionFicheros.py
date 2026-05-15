import os
import pickle


class GestionFicheros:

    @staticmethod
    def guardar_en_persistencias(dato, ruta):
        try:
            with open(ruta, 'ab') as persistencia:
                pickle.dump(dato, persistencia)

            return True

        except FileNotFoundError:
            return False

    @staticmethod
    def leer_persistencias(ruta):
        datos = []

        try:
            with open(ruta, 'rb') as persistencia:
                while True:
                    try:
                        dato = pickle.load(persistencia)
                        datos.append(dato)
                    except EOFError:
                        break

            return datos

        except FileNotFoundError:
            return []


    @staticmethod
    def resetear_persistencias():
        rutas = [
            "Persistencias/vehiculos/coches_datos",
            "Persistencias/vehiculos/furgonetas_datos",
            "Persistencias/vehiculos/motos_datos",
            "Persistencias/alquileres_datos",
            "Persistencias/clientes_datos",
            "Persistencias/sede_datos",
            "Persistencias/trabajadores_datos"
        ]

        for ruta in rutas:
            carpeta = os.path.dirname(ruta)

            if carpeta != "":
                os.makedirs(carpeta, exist_ok=True)

            with open(ruta, "wb") as archivo:
                pass

        return True

