# importar modulos de python
import socket
import os
import time
# import venv
import subprocess
import site
import sys

# importar modulos instalados


# importar modulos propios
from Preguntas import preguntas
from Direcciones import direcciones


def obtenerNetwork():
    # obtener el nombre de la red wifi
    return subprocess.run(["iwgetid", "-r"], capture_output=True, text=True).stdout.strip()


def obtenerIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    miIP = s.getsockname()[0]
    s.close()
    return miIP


def activate_venv():
    """
    Activate a Python virtual environment inside the current script.
 
    Args:
        venv_path (str): Path to the virtual environment folder.
                         e.g., "source/env"
    """
    # Determine Python version

    venv_path = "/home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/simple/env"

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


def enviarMensaje(ip, puerto, etiqueta, valor):
    pass


def default_handler(raspi, address, *args):
    # detectar si address es para chicas, medianas o grandes
    if (address.startswith(str("/paraChicas/"))):
        print("mensaje para chicas")
    elif (address.startswith(str("/paraMedianas/"))):
        print("mensaje para medianas")
    elif (address.startswith(str("/paraGrandes/"))):
        print("mensaje para grandes")


def handlerPantallas(direccion):
    comando = ""
    comando = direccion["comandoPrefijo"] + "001" + direccion["comandoSufijo"]
    os.system(comando)


def iniciar(ip):
    # si eres raspi principal
    if 0 != direcciones[ip][eje]:
        pass
    # si eres raspi con pantalla, haz esto otro
    else:
        dispatcher = Dispatcher()

        dispatcher.set_default_handler(handlerPantallas(direcciones[ip]))
        server = osc_server.ThreadingOSCUDPServer(
            (ip,
             1234), dispatcher)
        server.serve_forever()



while obtenerNetwork() != "TP-LINK_A9A4":
    print("no estoy en la red TP-LINK_A9A4, esperando...")
    print(len(obtenerNetwork()))
    print(len("TP-LINK_A9A4"))
    time.sleep(5)

activate_venv()

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from pythonosc.udp_client import SimpleUDPClient

miIP = obtenerIP()
print("mi IP es: " + str(obtenerIP()))


if (miIP in direcciones):
    print("mi direccion esta en el diccionario de direcciones")
    print("soy: " + str(direcciones[miIP]["descripcion"]))
    iniciar(direcciones[miIP]["eje"], direcciones[miIP]["tipoPantalla"], direcciones[miIP]["numero"])

else:
    print("mi direccion NO esta en el diccionario de direcciones")
    print("mi IP es: " + str(miIP))
    print("saliendo...")
    exit()
