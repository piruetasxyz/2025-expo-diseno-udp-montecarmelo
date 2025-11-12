# importar modulos de python
import socket
import os
import time
import subprocess
import site
import sys
import random

# importar modulos instalados
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from pythonosc.udp_client import SimpleUDPClient

# importar modulos propios
from Direcciones import direcciones

# variables globales
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

def enviarMensajeTodos(etiqueta, valor, clientes):
    for cliente in clientes:
        print(cliente)
        try:
            enviarMensaje(cliente, etiqueta, valor)
        except Exception as e:
            print("Error al enviar mensaje a " + str(cliente) + ": " + str(e))


def enviarMensaje(cliente, etiqueta, valor):
    cliente.send_message(etiqueta, valor)


def activate_venv(principal=False):

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


def handlerPantallas(direccion, *args):
    if args.startswith(str("/admin/init/")):
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
    # RASPI PRINCIPAL
    if direcciones[ip]["eje"] == 0:
        clientes = []
        for direccion in direcciones.keys():
            if (direcciones[direccion]["eje"] != 0):
                print("agregarClientes con ip: " + direccion)
                clientes.append(SimpleUDPClient(direccion, 1234))
        print(clientes)
        enviarMensajeTodos("/macbook/reboot/", 1, clientes)


miIP = obtenerIP()
print("mi IP es: " + str(obtenerIP()))

try:
    print("soy principal")
    activate_venv(principal=True)
except Exception as e:
    print("error", e)


if (miIP in direcciones.keys()):
    print("mi direccion esta en el diccionario de direcciones")
    print("soy: " + str(direcciones[miIP]["descripcion"]))
    iniciar(miIP)

else:
    print("mi direccion NO esta en el diccionario de direcciones")
    print("mi IP es: " + str(miIP))
    print("saliendo...")
    exit()
