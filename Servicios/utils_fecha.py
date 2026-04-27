from datetime import datetime,date
from typing import Optional

# convierte una str en formato dd%mm%yyyy en un objeto de la clase date
def string_a_fecha(fecha_str:str)-> Optional[date]:
    try:
        return datetime.strptime(fecha_str, "%d-%m-%Y").date()
    except (ValueError, TypeError):
        return None

def diferecia_dias(fecha1:date,fecha2:date)->Optional[int]:
    if isinstance(fecha1,date) and isinstance(fecha2,date):
        diferencia=fecha1-fecha2
        return diferencia.days
    return None