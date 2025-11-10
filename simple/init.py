# importar modulos de python
import os
import socket
import subprocess
import time
import venv


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
    os.chdir("/home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/")
    try:
        # hacer git pul
        os.system("git pull")
    except Exception as e:
        print(f"Error al hacer git pull: {e}")


def crearVirtualEnv():
    try:
        venvDir = "/home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/simple/env"
        venv.create(venvDir, with_pip=True)
        venvPython = os.path.join(venvDir, "bin", "python3")
        subprocess.run([venvPython, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.run([venvPython, "-m", "pip", "install", "-r", "/home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/simple/requirements.txt"])
    except Exception as e:
        print(f"Error al instalar dependencias: {e}")


# while obtenerNetwork() != "TP-LINK_A9A4":
#     print("no estoy en la red TP-LINK_A9A4, esperando...")
#     time.sleep(5)

miIP = obtenerIP()

print("mi IP es: " + str(obtenerIP()))
gitPull()
crearVirtualEnv()
