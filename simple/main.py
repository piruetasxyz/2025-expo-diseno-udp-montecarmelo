# importar modulos de python
import socket
import os
import time
import subprocess
import site
import sys
import random

# importar modulos instalados


# importar modulos propios
from Preguntas import preguntas
from Direcciones import direcciones

clientes = []




def obtenerNetwork():
    # obtener el nombre de la red wifi
    return subprocess.run(["iwgetid", "-r"], capture_output=True, text=True).stdout.strip()


def obtenerIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    miIP = s.getsockname()[0]
    s.close()
    return miIP


def enviarMensajeTodos(etiqueta, valor):
    for cliente in clientes:
        enviarMensaje(cliente, etiqueta, valor)


def enviarMensaje(cliente, etiqueta, valor):
    cliente.send_message(etiqueta, valor)


def activate_venv(principal=False):
    """
    Activate a Python virtual environment inside the current script.
 
    Args:
        venv_path (str): Path to the virtual environment folder.
                         e.g., "source/env"
    """

    venv_path = None

    if principal:
        venv_path = "/Users/" + os.getlogin() + "/github/2025-expo-diseno-udp-montecarmelo/simple/env"
    else:

        venv_path = "/home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/simple/env"
   
    # Determine Python version
    python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"

    # Build path to site-packages in the venv
    site_packages = os.path.join(venv_path, "lib", python_version, "site-packages")

    if not os.path.isdir(site_packages):
        raise FileNotFoundError(f"Cannot find site-packages at: {site_packages}")

    # Add venv's site-packages to sys.path
    site.addsitedir(site_packages)

    # Optionally, adjust sys.executable (useful in some cases)
    sys.executable = os.path.join(venv_path, "bin", "python")

    print(f"Virtual environment activated: {venv_path}")


def default_handler(raspi, address, *args):
    # detectar si address es para chicas, medianas o grandes
    if (address.startswith(str("/paraChicas/"))):
        print("mensaje para chicas")
    elif (address.startswith(str("/paraMedianas/"))):
        print("mensaje para medianas")
    elif (address.startswith(str("/paraGrandes/"))):
        print("mensaje para grandes")
    elif (address.startswith(str("/desdeAdmin/"))):
        print("mensaje desde admin")


def handlerPantallas(direccion):
    if direccion.startswith(str("/admin/init/")):
        print("inicializando pantalla...")
    else:
        # video aleatorio dentro de la carpeta correspondiente
        if direccion["tipoPantalla"] == 1:
            carpeta = "/home/" + os.getlogin() + "/respuestas/"
            archivos = [
                os.path.join(carpeta, f)
                for f in os.listdir(carpeta)
                if not f.startswith('.')
                ]
            if archivos:
                archivo_aleatorio = random.choice(archivos)
                # el mismo archivo en ambas pantallas
                os.system('./dual_vlc.sh ' + archivo_aleatorio + ' ' + archivo_aleatorio)
                # os.system(comando)



def iniciar(ip):
    # si eres raspi principal
    if 0 == direcciones[ip]["eje"]:
        for ip in direcciones.keys():
            clientes.append(SimpleUDPClient(ip, 1234))
        enviarMensajeTodos("/admin/init", 1)
        pass
    # si eres raspi con pantalla, haz esto otro
    else:
        print("dispatcher!")
        dispatcher = Dispatcher()

        dispatcher.set_default_handler(handlerPantallas(direcciones[ip]))
        server = osc_server.ThreadingOSCUDPServer(
            (ip,
             1234), dispatcher)
        server.serve_forever()


# while obtenerNetwork() != "TP-LINK_A9A4":
#     print("no estoy en la red TP-LINK_A9A4, esperando...")
#     print(len(obtenerNetwork()))
#     print(len("TP-LINK_A9A4"))
#     time.sleep(5)

miIP = obtenerIP()
print("mi IP es: " + str(obtenerIP()))

if miIP in direcciones.keys() and direcciones[miIP]["eje"] == 0:
    print("soy principal")
    activate_venv(principal=True)
else:
    print("no soy principal")
    activate_venv()

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from pythonosc.udp_client import SimpleUDPClient


if (miIP in direcciones.keys()):
    print("mi direccion esta en el diccionario de direcciones")
    print("soy: " + str(direcciones[miIP]["descripcion"]))
    iniciar(miIP)

else:
    print("mi direccion NO esta en el diccionario de direcciones")
    print("mi IP es: " + str(miIP))
    print("saliendo...")
    exit()
