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


