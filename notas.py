def calcular_media(notas):
    return sum(notas) / len(notas)

def mostrar_resumen(notas):
    media = round(calcular_media(notas),2)
    print(f"Número de notas: {len(notas)}")
    print(f"Nota máxima: {max(notas)}")
    print(f"Nota mínima: {min(notas)}")
    print(f"Nota media: {media}")