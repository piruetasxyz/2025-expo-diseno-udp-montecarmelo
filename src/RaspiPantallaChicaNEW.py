import RaspiPantalla
from Direcciones import chicas
from Preguntas import preguntas, faltantes
import os
import random
import subprocess
import re


class RaspiPantallaChica(RaspiPantalla.RaspiPantalla):
    def __init__(self, eje, numero):
        super().__init__(eje, numero)
        self.tamano = "chica"
        self.maximoPantallas = 4

        # -----------------------------------
        # OLD COMMANDS (kept for reference)
        # -----------------------------------
        # self.comandoPrefijo = "vlc --fullscreen --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla1 = "vlc --no-one-instance --qt-fullscreen-screennumber='2' --qt-minimal-view   --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla2 = "vlc --no-one-instance --qt-fullscreen-screennumber='7' --qt-minimal-view   --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla1 = "vlc --video-x=0--video-y=0  --qt-minimal-view   --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # self.comandoPrefijoPantalla2 = "vlc --video-x=0 --video-y=3000 --qt-minimal-view   --no-sub-autodetect-file --no-video-title-show --play-and-exit './../respuestas/"
        # -----------------------------------

        # -----------------------------------
        # DETECT CONNECTED MONITORS
        # -----------------------------------
        self.monitores = self.detectar_monitores()
        print("Monitores detectados:", self.monitores)

        if len(self.monitores) >= 2:
            geom1 = self.monitores[0]
            geom2 = self.monitores[1]
        elif len(self.monitores) == 1:
            geom1 = self.monitores[0]
            geom2 = {"x": 1920, "y": 0}  # fallback for 2nd display
        else:
            geom1 = {"x": 0, "y": 0}
            geom2 = {"x": 1920, "y": 0}

        # -----------------------------------
        # VLC COMMAND PREFIXES (NO HW ACCEL)
        # -----------------------------------
        # note: '--avcodec-hw=none' disables hardware acceleration
        self.comandoPrefijoPantalla1 = [
            "vlc", "--no-one-instance", "--no-playlist-enqueue",
            "--qt-minimal-view", "--no-sub-autodetect-file",
            "--no-video-title-show", "--fullscreen",
            "--avcodec-hw=none",
            f"--video-x={geom1['x']}", f"--video-y={geom1['y']}"
        ]
        self.comandoPrefijoPantalla2 = [
            "vlc", "--no-one-instance", "--no-playlist-enqueue",
            "--qt-minimal-view", "--no-sub-autodetect-file",
            "--no-video-title-show", "--fullscreen",
            "--avcodec-hw=none",
            f"--video-x={geom2['x']}", f"--video-y={geom2['y']}"
        ]

        self.carpeta_videos = os.path.join(os.path.dirname(__file__), "../respuestas/")
        self.comandoSufijo = ".mp4"

        # -----------------------------------
        # OLD LISTA / DEBUG INFO
        # -----------------------------------
        # self.listaVideos = list(respuestas.keys())
        print("lista respuestas:", getattr(self, "listaVideos", []))
        # self.listaVideos = ["01"]

        self.comandoPantalla1 = None
        self.comandoPantalla2 = None
        self.numeroRespuesta1 = None
        self.numeroRespuesta2 = None

        # -----------------------------------
        # DETERMINE IP
        # -----------------------------------
        print("recuperando ip")
        if (self.eje == 1):
            print("aqui con eje 1")
            self.direccionIP = chicas["eje-1"][self.numero]
        elif (self.eje == 2):
            print("aqui con eje 2")
            self.direccionIP = chicas["eje-2"][self.numero]
        elif (self.eje == 3):
            print("aqui con eje 3")
            self.direccionIP = chicas["eje-3"][self.numero]

    # -----------------------------------
    # HELPER: Detect monitors using xrandr
    # -----------------------------------
    def detectar_monitores(self):
        monitores = []
        try:
            salida = subprocess.check_output(["xrandr"]).decode("utf-8")
            # Match: HDMI-1 connected 1920x1080+0+0
            patron = re.compile(r"(\S+) connected.*?(\d+)x(\d+)\+(\d+)\+(\d+)")
            for nombre, ancho, alto, x, y in patron.findall(salida):
                monitores.append({
                    "nombre": nombre,
                    "ancho": int(ancho),
                    "alto": int(alto),
                    "x": int(x),
                    "y": int(y)
                })
            if not monitores:
                monitores = [{"nombre": "HDMI-1", "x": 0, "y": 0},
                             {"nombre": "HDMI-2", "x": 1920, "y": 0}]
        except Exception as e:
            print("Error detectando monitores:", e)
            monitores = [{"nombre": "HDMI-1", "x": 0, "y": 0},
                         {"nombre": "HDMI-2", "x": 1920, "y": 0}]
        return monitores

    # -----------------------------------
    # MAIN HANDLER
    # -----------------------------------
    def default_handler(self, address, *args):
        if (address.startswith("/paraChicas/nuevaRespuesta")):
            print("soy handler de la chicaaa")
            if (args is not None):
                print(preguntas[args[0]]["respuestas"])
                if (self.eje == 1):
                    respuestas_eje = preguntas[args[0]]["respuestas"]["eje-1"]
                    if len(respuestas_eje) > 0:
                        self.numeroRespuesta1 = random.choice(respuestas_eje)
                        self.numeroRespuesta2 = random.choice(respuestas_eje)
                    else:
                        self.numeroRespuesta1 = None
                        self.numeroRespuesta2 = None

                    if (self.numeroRespuesta1 not in faltantes):
                        path1 = os.path.join(self.carpeta_videos, f"{self.numeroRespuesta1}{self.comandoSufijo}")
                        print("Pantalla 1 →", path1)
                        subprocess.Popen(self.comandoPrefijoPantalla1 + [path1])
                    if (self.numeroRespuesta2 not in faltantes):
                        path2 = os.path.join(self.carpeta_videos, f"{self.numeroRespuesta2}{self.comandoSufijo}")
                        print("Pantalla 2 →", path2)
                        subprocess.Popen(self.comandoPrefijoPantalla2 + [path2])

                elif (self.eje == 2):
                    print(preguntas[args[0]]["respuestas"]["eje-2"])
                elif (self.eje == 3):
                    print(preguntas[args[0]]["respuestas"]["eje-3"])

    # -----------------------------------
    # DEBUG OUTPUT
    # -----------------------------------
    def mostrarEscena(self, escena):
        print(
            "pantalla chica, eje " +
            str(self.convertirComputadorHumano(self.eje)) +
            ", numero " + str(self.convertirComputadorHumano(self.numero)) +
            " de un maximo de " + str(self.maximoPantallas) +
            ", escena: " + str(self.convertirComputadorHumano(escena))
        )
