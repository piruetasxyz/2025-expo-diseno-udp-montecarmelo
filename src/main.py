# codig por montoyamoraga
# correr desde terminal
# con python3
# usar 2 argumentos numericos

# print("importando bibliotecas")
import sys
import Admin
import Raspi

# print(sys.argv)

if len(sys.argv) == 3:
    argumento1 = sys.argv[1]
    argumento2 = sys.argv[2]

    if int(argumento1) == 0:
        print("soy raspi admin")

    elif int(argumento1) == 1:
        print("soy raspi pantalla chica")

    elif int(argumento1) == 2:
        print("soy raspi pantalla mediana")

    elif int(argumento1) == 3:
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
