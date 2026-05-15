
import os
import pickle


class GestionFicheros:
    CARPETA = "Persistencias"

    FICHEROS = {
        "clientes": "clientes.dat",
        "sedes": "sedes.dat",
        "trabajadores": "trabajadores.dat",
        "alquileres": "alquileres.dat"
    }

    @staticmethod
    def crear_ficheros():
        os.makedirs(GestionFicheros.CARPETA, exist_ok=True)

        for nombre_fichero in GestionFicheros.FICHEROS.values():
            ruta = os.path.join(GestionFicheros.CARPETA, nombre_fichero)

            if not os.path.exists(ruta):
                with open(ruta, "wb") as fichero:
                    pickle.dump([], fichero)
x=GestionFicheros()
x.crear_ficheros()