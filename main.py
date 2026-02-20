import clases as cl

if __name__=='__main__':
    coche1=cl.Vehiculo('7432BFC','Honda','Civiv 1,6 vtec','Gris',40,'gasolina',40)

    coche1.echar_gasolina(30)
    print(coche1.gasolina)

    coche2=cl.Vehiculo('1234ZKI','Mazda','R8','Rojo',60,'eléctrico',60)
    coche2.echar_gasolina(20)
    coche2.mostrar_averias()

    persona1=cl.Cliente('72859472E','Alvaro','Castillo')
    persona2 = cl.Cliente('23890754U', 'Samuel', 'Ferrández')
    print(persona1.vehiculos)


    trabajador1=cl.Trabajador('3123123D','Pepe','Cremales','Sueldo',1500)

    alquiler1=cl.Alquiler(persona1,coche1,10,trabajador1)
    print(alquiler1.precio_alquiler())
    print(persona1.vehiculos[0].matricula)

