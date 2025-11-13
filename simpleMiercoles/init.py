# importar modulos de python
import os
import socket
import subprocess
import time
import venv
from Direcciones import direcciones


def obtenerIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    miIP = s.getsockname()[0]
    s.close()
    return miIP


def chmodear(ip):
    try:
        # cambiar permisos de los archivos del proyecto
        # if direcciones[ip]["eje"] != 0:
        os.system("chmod +x /home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/simple/vlc_on_screen.sh")
    except Exception as e:
        print(f"Error al chmodear vlc_on_screen.sh: {e}")
    try:
        os.system("chmod +x /Users/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/simple/dual_vlc.sh")
    except Exception as e:
        print(f"Error al chmodear dual_vlc.sh: {e}")

def gitPull(ip):
    try:
        # if direcciones[direcciones[ip]]["eje"] != 0:
        # ir al directorio del proyecto
        os.chdir("/home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/")
        # hacer git pul
        os.system("git pull")
    except Exception as e:
        print(f"Error al hacer git pull: {e}")

    try:
        # ir al directorio del proyecto
        os.chdir("/Users/" + os.getlogin() + "/github/2025-expo-diseno-udp-montecarmelo/")
        # hacer git pul
        os.system("git pull")
    except Exception as e:
        print(f"Error al hacer git pull: {e}")


def random_subfolder(path):
    # List all entries in the directory
    entries = os.listdir(path)
    
    # Keep only subfolders
    subfolders = [f for f in entries if os.path.isdir(os.path.join(path, f))]
    
    if not subfolders:
        raise ValueError("No subfolders found in the given path.")
    
    # Pick one randomly
    return os.path.join(path, random.choice(subfolders))

def crearVirtualEnv(ip):
    try:
        venvDir = "/home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/simple/env"
        venv.create(venvDir, with_pip=True)
        venvPython = os.path.join(venvDir, "bin", "python3")
        subprocess.run([venvPython, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.run([venvPython, "-m", "pip", "install", "-r", "/home/" + os.getlogin() + "/2025-expo-diseno-udp-montecarmelo/simple/requirements.txt"])
    except Exception as e:
        print(f"Error al instalar dependencias: {e}")
    try:
        venvDir = "/Users/" + os.getlogin() + "/github/2025-expo-diseno-udp-montecarmelo/simple/env"
        venv.create(venvDir, with_pip=True)
        venvPython = os.path.join(venvDir, "bin", "python3")
        subprocess.run([venvPython, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.run([venvPython, "-m", "pip", "install", "-r", "/Users/" + os.getlogin() + "/github/2025-expo-diseno-udp-montecarmelo/simple/requirements.txt"])
    except Exception as e:
        print(f"Error al instalar dependencias: {e}")


miIP = obtenerIP()
chmodear(miIP)
print("mi IP es: " + str(obtenerIP()))
gitPull(miIP)
crearVirtualEnv(miIP)
