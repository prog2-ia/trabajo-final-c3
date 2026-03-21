class GestionMantenimiento:
    def __init__(self,gestion_Sede):
        self.Gestion_Sede=gestion_Sede
        self.vehiculos_averiados=[]

    def añadir_avería(self,averia,matricula):
        vehiculo=self.Gestion_Sede.buscar_vehiculo(matricula)
        averias = ["Fallo de motor", "Problema de frenos", "Batería descargada", "Cambio de aceite",
                   "Neumático pinchado", "Problema en la transmisión", "Fallo eléctrico", "Radiador dañado",
                   "Filtro de aire sucio", "Correa de distribución rota"]
        if averia not in averias:
            return False
        elif vehiculo==None:
            return False
        else:
            for i in vehiculo.averias:
                if averia==i:
                    return False
            vehiculo.averias.append(averia)
            self.vehiculos_averiados.append(vehiculo)
            return True
    def reparar_vehiculo(self,matricula):
        vehiculo = self.Gestion_Sede.buscar_vehiculo(matricula)
        if vehiculo == None:
            return False
        else:
            if vehiculo.averias==[]:
                return False
            else:
                vehiculo.averias=[]
                coste=self.calcular_coste(matricula)
                return coste

    def calcular_coste(self,matricula):
        vehiculo = self.Gestion_Sede.buscar_vehiculo(matricula)
        if vehiculo == None:
            return None
        averias_costos = {
            "Fallo de motor": 1200,
            "Problema de frenos": 350,
            "Batería descargada": 100,
            "Cambio de aceite": 80,
            "Neumático pinchado": 60,
            "Problema en la transmisión": 900,
            "Fallo eléctrico": 450,
            "Radiador dañado": 500,
            "Filtro de aire sucio": 40,
            "Correa de distribución rota": 700
        }
        coste=0
        for i in vehiculo.averias:
            coste+=averias_costos[i]
        return coste  #Si el costo es 0, el vehiculo no tenía averias
