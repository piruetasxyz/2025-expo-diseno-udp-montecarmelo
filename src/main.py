# correr desde terminal
# con python3
# usar 3 argumentos numericos

# uso
# python3 main.py eje tipo numero
# donde
# eje = eje, 1, 2, 3
# tipo = tipo de raspi, 0=admin, 1=chica, 2=mediana, 3=grande
# numero = numero de raspi en ese eje, depende del eje, puede ser entre 1 y 4


import sys
from Admin import Admin

admin = Admin()

if len(sys.argv) != 4:
    print("error en argumentos")
    print("uso: python3 main.py eje tipo numero")
    print("donde")
    print("eje: 1, 2, 3")
    print("tipo: 0=admin, 1=chica, 2=mediana, 3=grande")
    print("numero de raspi en ese eje, entre 1 y 4")
    sys.exit()

else:
    argumento1Eje = int(sys.argv[1])
    argumento2Tipo = int(sys.argv[2])
    argumento3Numero = int(sys.argv[3])

    # crear administrador en la raspi
    # si argumento1 es 0, crear cliente raspi principal y buclear
    if int(argumento2Tipo) == 0:
        admin.crearPrincipal()
        admin.buclear()
        # print("soy raspi servidor")

    elif int(argumento2Tipo) == 1:
        admin.crearChica(argumento1Eje, argumento3Numero)
        # raspiChica = RaspiPantallaChica(argumento2, 1)
        # raspiChica.handler()
        # print("soy raspi pantalla chica")

    elif int(argumento2Tipo) == 2:
        admin.crearMediana(argumento1Eje, argumento3Numero)
        #   raspiMediana = RaspiPantallaMediana(argumento2, 1)
        # raspiMediana.handler()
        # print("soy raspi pantalla mediana")

    elif int(argumento2Tipo) == 3:
        admin.crearGrande(argumento1Eje, argumento3Numero)
        # raspiGrande = RaspiPantallaGrande(argumento2, 1)
        # raspiGrande.handler()
        # print("soy raspi pantalla grande")
    else:
        print("mi argumento no tiene sentido")

    # if int(argumento2Tipo) != 0:
    #     if int(argumento1Eje) == 1:
    #         print("soy del eje 1")
    #     elif int(argumento1Eje) == 2:
    #         print("soy del eje 2")
    #     elif int(argumento1Eje) == 3:
    #         print("soy del eje 3")
