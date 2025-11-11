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
from Preguntas import preguntas
from Datos import datos
from Direcciones import direcciones



# variables globales
clientes = []
pizca = 1.01
generativasH = [
    "horizontal-1-arica/",
    "horizontal-2-antofagasta/",
    "horizontal-3-valpo/",
    "horizontal-4-aysen/",
    "horizontal-5-magallanes/"
    ]
generativasV = [
    "vertical-1-arica/",
    "vertical-2-antofagasta/",
    "vertical-3-valpo/",
    "vertical-4-aysen/",
    "vertical-5-magallanes/"     
]

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
            if (direccion["eje" != 0]):
                print("agregarClientes con ip: " + direccion)
                clientes.append(SimpleUDPClient(direccion, 1234))
        print(clientes)
        enviarMensajeTodos("/admin/init/", 1, clientes)
        enviarMensajeTodos("/medianas/mostrarEjes/", 1, clientes)
        # pausa de 2 segundos antes de empezar el cicllo
        time.sleep(2 * pizca)

        while True:
            # 000s = 00m00s
            # TODAS GENERATIVAS
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 010s = 00m10s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 020s = 00m20s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 030s = 00m30s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 040s = 00m40s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 050s = 00m50s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 060s = 01m
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 070s = 01m10s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 080s = 01m20s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 090s = 01m30s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 100s = 01m40s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 110s = 01m50s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 120s = 02m00s
            enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            # 130s = 02m10s
            # 140s = 02m20s
            # 150s = 02m30s
            # 160s = 02m40s
            # 170s = 02m50s
            # 180s = 03m00s
            # 190s = 03m10s
            # 200s = 03m20s
            # 210s = 03m30s
            # 220s = 03m40s
            # 230s = 03m50s
            # 240s = 04m00s
            # 250s = 04m10s
            # 260s = 04m20s
            # 270s = 04m30s
            # 280s = 04m40s
            # 290s = 04m50s
            # 300s = 05m00s
            # 310s = 05m10s
            # 320s = 05m20s
            # 330s = 05m30s
            # 340s = 05m40s
            # 350s = 05m50s
            # 360s = 06m00s
            # 370s = 06m10s
            # 380s = 06m20s
            # 390s = 06m30s
            # 400s = 06m40s
            # 410s = 06m50s
            # 420s = 07m00s
            # 430s = 07m10s
            # 440s = 07m20s
            # 450s = 07m30s
            # 460s = 07m40s
            # 470s = 07m50s
            # 480s = 08m00s
            # 490s = 08m10s
            # 500s = 08m20s
            # 510s = 08m30s
            # 520s = 08m40s
            # 530s = 08m50s
            # 540s = 09m00s
            # 550s = 09m10s
            # 560s = 09m20s
            # 570s = 09m30s
            # 580s = 09m40s
            # 590s = 09m50s
            # 600s = 10m00s
             # FIN DE CICLO
            # 00s
            # enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            # enviarMensajeTodos("/medianas/mostrarGenerativas/", 1, clientes)
            # enviarMensajeTodos("/chicas/mostrarGenerativas/", 1, clientes)
            # # 10s
            # # todas pausan por 10 segundos
            # time.sleep(10 * pizca)
            # # elegimos la primera pregunta aleatoria
            # # las grandes siguen mostrando generativas

            # # las medianas horizontales muestran pregunta
            # # las medianas verticales muestran eje
            # # las chicas muestran respuestas aleatorias
            # # esto pasa por 5 minutos
            # time.sleep(5 * 60 * pizca)
            # # elegimos una segunda pregunta aleatoria
            # # esto pasa por 5 minutos
            # time.sleep(5 * 60 * pizca)

    # si eres raspi con pantalla, haz esto otro
    else:
        print("dispatcher!")
        dispatcher = Dispatcher()

        # si eres pantalla chica
        if direcciones[ip]["tipoPantalla"] == 1:
            dispatcher.set_default_handler(handlerChicas)
        # si es una pantalla de 32 pulgadas
        elif direcciones[ip]["tipoPantalla"] == 2:
            # si es la mediana 1, es horizontal y muestra pregunta
            if direcciones[ip]["numero"] == 1:
                dispatcher.set_default_handler(handlerMedianas1Horizontal)
            # si es la mediana 2, es vertical y muestra eje
            elif direcciones[ip]["numero"] == 2:
                dispatcher.set_default_handler(handlerMedianas2Vertical)
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

        print(direcciones[miIP]["comandoGenerativa"] + archivo + "'")
        os.system(direcciones[miIP]["comandoGenerativa"] + archivo + "'")


def handlerMedianas1Horizontal(address, *args):
    pass


def handlerMedianas2Vertical(address, *args):
    print(address)
    if address.startswith("/medianas/mostrarEjes/"):
        comando = direcciones[miIP]["comandoPrefijo"] + "/home/" + os.getlogin() + "/ejes/eje" + str(direcciones[miIP]["eje"]) + ".mp4'"
        print(comando)
        os.system(comando)


# pantallas grandes, son 3, una por eje
def handlerGrandes(address, *args):
    print(address)
    if address.startswith("/grandes/"):
        print("llega un mensaje a grande")
        if address.startswith("/grandes/mostrarGenerativas/"):   
            carpetaHRandom = random.choice(generativasH)
            subCarpeta = "/home/" + os.getlogin() + "/generativas/" + carpetaHRandom
            print(subCarpeta)
            archivo = random_file_in_folder(subCarpeta)
            print(direcciones[miIP]["comandoGenerativa"] + archivo + "'")
            os.system(direcciones[miIP]["comandoGenerativa"] + archivo + "'")

    # else:
        # print("mensaje no reconocido en grande")
    # if address.startswith("/mostrarGenerativas/"):
    #     subCarpeta = None

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

# from pythonosc.dispatcher import Dispatcher
# from pythonosc import osc_server
# from pythonosc.udp_client import SimpleUDPClient


if (miIP in direcciones.keys()):
    print("mi direccion esta en el diccionario de direcciones")
    print("soy: " + str(direcciones[miIP]["descripcion"]))
    iniciar(miIP)

else:
    print("mi direccion NO esta en el diccionario de direcciones")
    print("mi IP es: " + str(miIP))
    print("saliendo...")
    exit()
