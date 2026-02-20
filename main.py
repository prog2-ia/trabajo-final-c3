import clases as cl

if __name__=='__main__':
    coche1=cl.Vehiculo('7432BFC','Honda','Civiv 1,6 vtec','Gris',40,'gasolina')

    coche1.hechar_gasolina(30)
    print(coche1.gasolina)

    persona1=cl.Persona('72859472E','Alvaro','Castillo','no')
    persona2 = cl.Persona('23890754U', 'Samuel', 'Ferrández', coche1)
    print(persona2.coche.marca)

    coche2=cl.Vehiculo('1234ZKI','Mazda','R8','Rojo',60,'eléctrico')
    coche2.echar_gasolina(20)
    print(coche2.marca)