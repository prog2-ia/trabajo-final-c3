from datetime import datetime


# convierte una str en formato dd%mm%yyyy en un objeto de la clase date
def string_a_fecha(fecha_str):
    return datetime.strptime(fecha_str, "%d-%m-%Y").date()

def diferecia_dias(fecha1,fecha2):
    if isinstance(fecha1,datetime) and isinstance(fecha2,datetime):
        diferencia=fecha1-fecha2
        return diferencia.days
    return None