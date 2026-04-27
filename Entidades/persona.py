class Persona:
    def __init__(self, dni:str, nombre:str, apellidos:str,telefono:int)->None:
        #if self.validar_dni(dni)==True and self.validar_movil(telefono)==True:
        self.nombre:str=nombre
        self.apellidos:str=apellidos
        self.telefono:int=telefono
        self._dni:str=dni

    @property
    def dni(self) -> str:
        return self._dni
#Función que valida dnis
    def validar_dni(self,DNI:str) -> bool:
        letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        dni=list(DNI)
        correcto=True
        numero=0
        if len(dni)==9:
            numeros=dni[0:8]
            for i in numeros:
                if not i.isdigit():
                    correcto=False
                else:
                    numero=numero*10
                    numero+=int(i)
            if dni[8].upper()!= letras[numero%23]:
                correcto=False
        else:
            correcto=False
        return correcto




#Función que valida el número de teléfono
    def validar_movil(self,telefono:int) -> bool:
        correcto=True
        if type(telefono)==type(4):
            if len(str(telefono))==9:
                correcto=True
            else:
                correcto=False
        else:
            correcto=False
        return correcto