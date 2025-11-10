# importar modulos de python
import socket
import os
import time

# importar modulos instalados
import python-osc

# importar modulos propios
from Preguntas import preguntas

def obtenerNetwork():
    # obtener el nombre de la red wifi
    return os.system("iwgetid -r")


def obtenerIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    miIP = s.getsockname()[0]
    s.close()
    return miIP


def gitPull():

    # ir al directorio del proyecto
    os.chdir("/home/pi/2025-expo-diseno-udp-montecarmelo")
    try:
        # hacer git pul
        os.system("git pull")
    except Exception as e:
        print(f"Error al hacer git pull: {e}")


def crearVirtualEnv():
    os.chdir("/home/pi/2025-expo-diseno-udp-montecarmelo/simple")
    os.system("python3 -m venv venv")
    os.system("source venv/bin/activate")
    try:
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
    except Exception as e:
        print(f"Error al instalar dependencias: {e}")


def activarVirtualEnv():
    os.chdir("/home/pi/2025-expo-diseno-udp-montecarmelo/simple")
    os.system("source venv/bin/activate")


while obtenerNetwork() != "TP-LINK_A9A4":
    print("no estoy en la red TP-LINK_A9A4, esperando...")
    time.sleep(5)

print("mi IP es: " + str(obtenerIP()))
gitPull()
crearVirtualEnv()
activarVirtualEnv()