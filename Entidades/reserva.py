class Reserva:
    def __init__(self,fecha_inicio,fecha_fin):
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin

#Devuelcve True si dentro de un rango de 2 fechas coincide la reserva
    def coinciden_fechas(self, fecha_inicio_nueva, fecha_fin_nueva):
        if self.fecha_inicio < fecha_inicio_nueva < self.fecha_fin or self.fecha_inicio < fecha_fin_nueva < self.fecha_fin:
            return True
        return False