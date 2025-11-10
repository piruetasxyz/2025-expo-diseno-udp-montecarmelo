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
from Datos import datos
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


def random_subfolder(path):
    # List all entries in the directory
    entries = os.listdir(path)

    # Keep only subfolders
    subfolders = [f for f in entries if os.path.isdir(os.path.join(path, f))]

    if not subfolders:
        raise ValueError("No subfolders found in the given path.")

    # Pick one randomly
    return os.path.join(path, random.choice(subfolders))


def random_file_in_folder(folder_path):
    # Get all files (ignore subfolders)
    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        raise ValueError("No files found in the folder.")

    # Choose one randomly
    return os.path.join(folder_path, random.choice(files))


def random_file_in_subfolder(base_path):
    # List all subfolders
    subfolders = [f for f in os.listdir(base_path)
                  if os.path.isdir(os.path.join(base_path, f))]

    if not subfolders:
        raise ValueError("No subfolders found in the given path.")

    # Pick a random subfolder
    chosen_subfolder = random.choice(subfolders)
    subfolder_path = os.path.join(base_path, chosen_subfolder)

    # List files inside that subfolder
    files = [f for f in os.listdir(subfolder_path)
             if os.path.isfile(os.path.join(subfolder_path, f))]

    if not files:
        raise ValueError(f"No files found in subfolder: {chosen_subfolder}")

    # Pick a random file
    random_file = random.choice(files)
    return os.path.join(subfolder_path, random_file)


def enviarMensajeTodos(etiqueta, valor, clientes):
    for cliente in clientes:
        print(cliente)
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
    # si eres raspi principal
    if direcciones[ip]["eje"] == 0:
        clientes = []
        for direccion in direcciones.keys():
            print("agregarClientes con ip: " + direccion)
            clientes.append(SimpleUDPClient(direccion, 1234))
        enviarMensajeTodos("/admin/init/", 1, clientes)

        while True:
            enviarMensajeTodos("/mostrarGenerativas/", 1, clientes)
            time.sleep(5)

    # si eres raspi con pantalla, haz esto otro
    else:
        print("dispatcher!")
        dispatcher = Dispatcher()
        
        # si eres pantalla chica
        if direcciones[ip]["tipoPantalla"] == 1:
            dispatcher.set_default_handler(handlerChicas)
        elif direcciones[ip]["tipoPantalla"] == 2:
            dispatcher.set_default_handler(handlerMedianas)
        elif (direcciones[ip]["tipoPantalla"]) == 3:
            dispatcher.set_default_handler(handlerGrandes)

        server = osc_server.ThreadingOSCUDPServer(
            (ip,
             1234), dispatcher)
        server.serve_forever()


def handlerChicas(address, *args):
    print(address)
    if address.startswith("/mostrarGenerativas/"):
        subCarpeta = random_subfolder("/home/" + os.getlogin() + "/generativas/")
        print(subCarpeta)
        archivo = random_file_in_folder(subCarpeta)

        print(direcciones[miIP]["comandoGenerativa"] + archivo
        os.system(direcciones[miIP]["comandoGenerativa"] + archivo


def handlerMedianas(address, *args):
    print(address)
    pass


def handlerGrandes(address, *args):
    print(address)
    pass


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
