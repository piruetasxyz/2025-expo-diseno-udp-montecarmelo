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
from Preguntas import preguntas, duracionesRespuestas, faltantes, negras
from Direcciones import direcciones


# variables globales
clientes = []
pizca = 1.0001
probabilidadRespuesta = 1.0

generativas = {
    "arica": ["horizontal-1-arica/",
              "vertical-1-arica"],
    "antofagasta": ["horizontal-2-antofagasta/",
                    "vertical-2-antofagasta"],
    "valpo": ["horizontal-3-valpo/",
              "vertical-3-valpo"],
    "aysen": ["horizontal-4-aysen/",
              "vertical-4-aysen"],
    "magallanes": ["horizontal-5-magallanes/",
                   "vertical-5-magallanes"]
}


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

    # Get all files that don't start with "._"
    files = [f for f in os.listdir(folder_path)
             if not f.startswith(".") and os.path.isfile(os.path.join(folder_path, f))]

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
            if (direccion["eje"] != 0):
                print("agregarClientes con ip: " + direccion)
                clientes.append(SimpleUDPClient(direccion, 1234))
        print(clientes)
        # enviarMensajeTodos("/admin/init/", 1, clientes)
        # enviarMensajeTodos("/medianas/vertical/mostrarEjes/", 1, clientes)
        # pausa de 2 segundos antes de empezar el cicllo
        time.sleep(2 * pizca)

        while True:
            # 000s = 00m00s
            # TODAS GENERATIVAS
            genRandom = random.choice(list(generativas.keys()))
            
            enviarMensajeTodos("/medianas/mostrarGenerativas/", genRandom, clientes)
            enviarMensajeTodos("/chicas/mostrarGenerativas/", genRandom, clientes)
            enviarMensajeTodos("/grandes/mostrarGenerativas/", genRandom, clientes)
            time.sleep(10 * pizca)
            # 010s = 00m10s
            # enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            # enviarMensajeTodos("/medianas/vertical/mostrarEjes/", 1, clientes)
            # choose random number between 1 and 21
            pregunta1 = random.randint(1, 21)
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            enviarMensajeTodos("/medianas/vertical/mostrarEjes/", 1, clientes)
            enviarMensajeTodos("/medianas/horizontal/mostrarPreguntas/", pregunta1, clientes)
            enviarMensajeTodos("/grandes/mostrarTextos/", 1, clientes)
            time.sleep(10 * pizca)
            # 020s = 00m20s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 030s = 00m30s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 040s = 00m40s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 050s = 00m50s
            
            time.sleep(10 * pizca)
            # 060s = 01m
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 070s = 01m10s
            
            time.sleep(10 * pizca)
            # 080s = 01m20s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 090s = 01m30s
            
            time.sleep(10 * pizca)
            # 100s = 01m40s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 110s = 01m50s
            
            time.sleep(10 * pizca)
            # 120s = 02m00s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 130s = 02m10s
            
            time.sleep(10 * pizca)
            # 140s = 02m20s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            
            # 150s = 02m30s
            time.sleep(10 * pizca)
            
            # 160s = 02m40s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            
            # 170s = 02m50s
            time.sleep(10 * pizca)
            
            # 180s = 03m00s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            
            # 190s = 03m10s
            
            time.sleep(10 * pizca)
            # 200s = 03m20s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 210s = 03m30s
            
            time.sleep(10 * pizca)
            # 220s = 03m40s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 230s = 03m50s
            
            time.sleep(10 * pizca)
            # 240s = 04m00s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 250s = 04m10s
            
            time.sleep(10 * pizca)
            # 260s = 04m20s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 270s = 04m30s
            
            time.sleep(10 * pizca)
            
            # 280s = 04m40s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 290s = 04m50s
            
            time.sleep(10 * pizca)
            # 300s = 05m00s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta1, clientes)
            time.sleep(10 * pizca)
            # 310s = 05m10s
            # MEDIANAS vertical mostrar ejes
            # enviarMensajeTodos("/grandes/mostrarGenerativas/", 1, clientes)
            time.sleep(10 * pizca)
            enviarMensajeTodos("/medianas/vertical/mostrarEjes/", 1, clientes)
            pregunta2 = random.randint(1, 21)
            enviarMensajeTodos("/medianas/horizontal/mostrarPreguntas/", pregunta2, clientes)
            
            time.sleep(10 * pizca)
            # 320s = 05m20s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 330s = 05m30s
            
            time.sleep(10 * pizca)
            # 340s = 05m40s
            
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 350s = 05m50s
            
            time.sleep(10 * pizca)
            # 360s = 06m00s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 370s = 06m10s
            time.sleep(10 * pizca)
            # 380s = 06m20s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 390s = 06m30s
            time.sleep(10 * pizca)
            # 400s = 06m40s
            time.sleep(10 * pizca)
            # 410s = 06m50s
            time.sleep(10 * pizca)
            # 420s = 07m00s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 430s = 07m10s
            time.sleep(10 * pizca)
            # 440s = 07m20s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 450s = 07m30s
            time.sleep(10 * pizca)
            # 460s = 07m40s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 470s = 07m50s
            time.sleep(10 * pizca)
            # 480s = 08m00s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 490s = 08m10s
            time.sleep(10 * pizca)
            # 500s = 08m20s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 510s = 08m30s
            time.sleep(10 * pizca)
            # 520s = 08m40s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 530s = 08m50s
            time.sleep(10 * pizca)
            # 540s = 09m00s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 550s = 09m10s
            time.sleep(10 * pizca)
            # 560s = 09m20s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 570s = 09m30s
            time.sleep(10 * pizca)
            # 580s = 09m40s
            enviarMensajeTodos("/chicas/mostrarRespuestas/", pregunta2, clientes)
            time.sleep(10 * pizca)
            # 590s = 09m50s
            time.sleep(10 * pizca)
            # 600s = 10m00s
            time.sleep(10 * pizca)
            # FIN DE CICLO
            # 00s
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
    if address.startswith("/chicas/mostrarRespuestas/"):
        # randomizar
        # if (random.random() < probabilidadRespuesta):
        if True:
            print("voy a tratar de mostrar una respuesta")
            # buscar respuestas correspondientes
            # respuestasPosibles = preguntas[args[0]]["respuestas"]["eje-" + str(direcciones[miIP]["eje"])]
            # PANA
            respuestasPosibles = preguntas[args[0]]["respuestas"]["eje-" + str(1)]
            respuestaAleatoria = random.choice(respuestasPosibles)
            # pathRespuestaAleatoria = "/home/" + os.getlogin() + "/respuestas/" + respuestaAleatoria + ".mp4"
            # OTRA PANA
            pathRespuestaAleatoria = random_file_in_folder("/home/" + os.getlogin() + "/respuestas/")
            # print("respuestasPosiblesDelEje:", respuestasPosibles)
            # print("pathRespuestaAleatoria:", pathRespuestaAleatoria)
            # comando para osSystem
            # elCOMANDO = './dual_vlc_respuestas.sh ' + pathRespuestaAleatoria + ' ' + pathRespuestaAleatoria   
            archivo = random_file_in_folder("/home/" + os.getlogin() + "/respuestas/")
            elCOMANDO = './dual_vlc_respuestas.sh ' + archivo + ' ' + archivo
            print("elCOMANDO:", elCOMANDO)
            os.system(elCOMANDO)
            # if (preguntas[args[0]]["respuestas"]):
            # respuestasPosibles = preguntas[args[0]]["respuestas"]

    elif address.startswith("/chicas/mostrarGenerativas/"):
        region = args[0]
        carpetaV = generativas[region][1]
        subCarpeta = "/home/" + os.getlogin() + "/generativas/" + carpetaV
        print("subcarpeta: " + subCarpeta)
        archivo = random_file_in_folder(subCarpeta)
        print("archivo: " + archivo)
        os.system('./dual_vlc_generativas.sh ' + archivo + ' ' + archivo)
        # print(direcciones[miIP]["comandoGenerativa"] + archivo + "'")
        # os.system(direcciones[miIP]["comandoGenerativa"] + archivo + "'")


def handlerMedianas1Horizontal(address, *args):
    print(address)
    # prints args
    print("args:", args)
    if address.startswith("/medianas/horizontal/mostrarPreguntas/"):
        #  pad it with one 0 if its less than 10
        num = str(args[0]).zfill(2)
        comando = direcciones[miIP]["comandoPrefijo"] + "/home/" + os.getlogin() + "/preguntas/" + num + ".mp4'"
        # print("comando", comando)
        os.system(comando)
    elif address.startswith("/medianas/mostrarGenerativas/"):
        region = args[0]
        carpetaH = generativas[region][0]
        subCarpeta = "/home/" + os.getlogin() + "/generativas/" + carpetaH
        # print(subCarpeta)
        archivo = random_file_in_folder(subCarpeta)
        print(direcciones[miIP]["comandoGenerativa"] + archivo + "'")
        os.system(direcciones[miIP]["comandoGenerativa"] + archivo + "'")


def handlerMedianas2Vertical(address, *args):
    print(address)
    if address.startswith("/medianas/vertical/mostrarEjes/"):
        comando = direcciones[miIP]["comandoPrefijo"] + "/home/" + os.getlogin() + "/ejes/eje" + str(direcciones[miIP]["eje"]) + ".mp4'"
        print(comando)
        os.system(comando)
    elif address.startswith("/medianas/mostrarGenerativas/"):
        region = args[0]
        carpetaV = generativas[region][1]
        subCarpeta = "/home/" + os.getlogin() + "/generativas/" + carpetaV
        # print(subCarpeta)
        archivo = random_file_in_folder(subCarpeta)
        print(direcciones[miIP]["comandoGenerativa"] + archivo + "'")
        os.system(direcciones[miIP]["comandoGenerativa"] + archivo + "'")


# pantallas grandes, son 3, una por eje
def handlerGrandes(address, *args):
    print(address)
    if address.startswith("/macbook/reboot/"):
        os.system("sudo reboot")
    elif address.startswith("/grandes/mostrarGenerativas/"):
        print("llega un mensaje a grande")
        if address.startswith("/grandes/mostrarGenerativas/"):
            region = args[0]
            carpetaH = generativas[region][0]
            subCarpeta = "/home/" + os.getlogin() + "/generativas/" + carpetaH
            print(subCarpeta)
            archivo = random_file_in_folder(subCarpeta)
            # print(direcciones[miIP]["comandoGenerativa"] + archivo + "'")
            os.system(direcciones[miIP]["comandoGenerativa"] + archivo + "'")
    elif address.startswith("/grandes/mostrarTextos/"):
        # print(direcciones[miIP]["comandoTexto"] + "texto-1" + direcciones[miIP]["comandoSufijoTexto"])
        esteCOMANDOGRANDE = direcciones[miIP]["comandoTexto"] + "/home/" + os.getlogin() + "/textos/texto-1" + direcciones[miIP]["comandoSufijoTexto"]
        print("esteCOMANDOGRANDE", esteCOMANDOGRANDE)
        os.system(esteCOMANDOGRANDE)

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
    try:
        print("soy principal")
        activate_venv(principal=True)
    except Exception as e:
        print("error", e)
else:
    try:
        print("no soy principal")
        activate_venv()
    except Exception as e:
        print("error", e)

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
