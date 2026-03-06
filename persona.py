class Persona:
    def __init__(self, dni, nombre, apellidos,telefono):
        if self.validar_dni(dni)==True and self.validar_movil(telefono)==True:
            self.dni=dni
            self.nombre=nombre
            self.apellidos=apellidos
            self.telefono=telefono
        else:
            print('El dni o el teléfono no es correcto')


    def validar_dni(self,DNI):
        letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        dni=list(DNI)
        correcto=True
        numero=0
        if len(dni)==9:
            numeros=dni[0:8]
            for i in numeros:
                if not i.isdigit:
                    correcto=False
                else:
                    numero=numero*10
                    numero+=int(i)
            if dni[8].upper()!= letras[numero%23]:
                correcto=False
        else:
            correcto=False
        return correcto





    def validar_movil(self,telefono):
        correcto=True
        if type(telefono)==type(4):
            if len(str(telefono))==9:
                correcto=True
            else:
                print('Teléfono incorrecto')
                correcto=False
        else:
            print('Teléfono incorrecto')
            correcto=False
        return correcto