def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero válido")

def pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: introduce un número válido")

def pedir_opcion(mensaje: str, opciones: list[int]) -> int:
    while True:
        try:
            op = int(input(mensaje))
            if op in opciones:
                return op
            print(f"Error: elige una opción entre {opciones[0]} y {opciones[-1]}")
        except ValueError:
            print("Error: introduce un número entero válido")



