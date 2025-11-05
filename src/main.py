# codig por montoyamoraga
# correr desde terminal
# con python3
# usar 2 argumentos numericos

# uso
# python3 main.py x y z
# donde
# x = tipo de raspi, 0=admin, 1=chica, 2=mediana, 3=grande
# y = eje, 1, 2, 3
# z = numero de raspi en ese eje, depende del eje, puede ser entre 0 y 4

# print("importando bibliotecas")
import sys
from Admin import Admin
from RaspiPantallaChica import RaspiPantallaChica
from RaspiPantallaMediana import RaspiPantallaMediana
from RaspiPantallaGrande import RaspiPantallaGrande

# print(sys.argv)

if len(sys.argv) != 4:
    print("error en argumentos")
    print("uso: python3 main.py x y z")
    print("donde")
    print("x = tipo de raspi, 0=admin, 1=chica, 2=mediana, 3=grande")
    print("y = eje, 1, 2, 3")
    print("z = numero de raspi en ese eje, depende del eje, puede ser entre 0 y 4")
    sys.exit()

else:
    argumento1 = sys.argv[1]
    argumento2 = sys.argv[2]
    argumento3 = sys.argv[3]

    if int(argumento1) == 0:
        admin = Admin()
        admin.crearCliente(5005)
        admin.buclear()
        print("soy raspi servidor")

    elif int(argumento1) == 1:
        raspiChica = RaspiPantallaChica(argumento2, 1)
        raspiChica.handler()
        print("soy raspi pantalla chica")

    elif int(argumento1) == 2:
        raspiMediana = RaspiPantallaMediana(argumento2, 1)
        raspiMediana.handler()
        print("soy raspi pantalla mediana")

    elif int(argumento1) == 3:
        raspiGrande = RaspiPantallaGrande(argumento2, 1)
        raspiGrande.handler()
        print("soy raspi pantalla grande")
    else:
        print("mi argumento no tiene sentido")

    if int(argumento1) != 0:
        if int(argumento2) == 1:
            print("soy del eje 1")
        elif int(argumento2) == 2:
            print("soy del eje 2")
        elif int(argumento2) == 3:
            print("soy del eje 3")
