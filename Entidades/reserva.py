from datetime import date

class Reserva:
    def __init__(self,fecha_inicio:date,fecha_fin:date)->None:
        self.fecha_inicio:date=fecha_inicio
        self.fecha_fin:date=fecha_fin

#Devuelve True si dentro de un rango de 2 fechas coincide la reserva
    def coinciden_fechas(self, fecha_inicio_nueva:date, fecha_fin_nueva:date) -> bool:
        if self.fecha_inicio < fecha_inicio_nueva < self.fecha_fin or self.fecha_inicio < fecha_fin_nueva < self.fecha_fin:
            return True
        return False